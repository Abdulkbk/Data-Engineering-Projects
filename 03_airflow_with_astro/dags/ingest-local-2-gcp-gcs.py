import os
import pendulum

from airflow.decorators import dag, task, task_group

from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator


months = ['01', '02', '03', '04']
dataset_file = "yellow_tripdata_2022-"
dataset_ext = ".parquet"
data_url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/"

path_to_local_home = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")

BUCKET_NAME = os.getenv("BUCKET_NAME", 'data-eng-lake')


default_args = {
  "owner": "admin",
  "start_date": pendulum.local(2022, 8, 13),
  "depends_on_past": False,
  "retries": 1,
}

@dag(
  schedule_interval="@monthly",
  default_args=default_args,
  tags=['data', 'ingestion']
)
def workflow():

  @task()
  def logger():
    print("Airflow to the data world")
    print("Download starting....")

  download_01_data = BashOperator(
    task_id="download_dataset_task_01",
    bash_command=f"curl -sSL {data_url}{dataset_file}01{dataset_ext} > {path_to_local_home}/{dataset_file}01{dataset_ext}"
  )

  download_02_data = BashOperator(
    task_id="download_dataset_task_02",
    bash_command=f"curl -sSL {data_url}{dataset_file}02{dataset_ext} > {path_to_local_home}/{dataset_file}02{dataset_ext}"
  )

  download_03_data = BashOperator(
    task_id="download_dataset_task_03",
    bash_command=f"curl -sSL {data_url}{dataset_file}03{dataset_ext} > {path_to_local_home}/{dataset_file}03{dataset_ext}"
  )

  download_04_data = BashOperator(
    task_id="download_dataset_task_04",
    bash_command=f"curl -sSL {data_url}{dataset_file}04{dataset_ext} > {path_to_local_home}/{dataset_file}04{dataset_ext}"
  )

  local2gcs = LocalFilesystemToGCSOperator(
    src=[f"{path_to_local_home}{i}" for i in os.listdir(f"{path_to_local_home}")],
    dst="/raw/yellow/",
    bucket=f"{BUCKET_NAME}",
    task_id="local2gcs",
    gcp_conn_id="google_cloud_default"
  )

  logger()
  [download_01_data >> download_02_data >> download_03_data >> download_04_data] >> local2gcs


workflow = workflow()

