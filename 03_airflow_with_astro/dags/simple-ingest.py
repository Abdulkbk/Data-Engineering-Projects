import os
import pendulum

from airflow.decorators import dag, task, task_group

from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator

DATA_URL = os.getenv("DATA_URL", r"https://sample-videos.com/csv/Sample-Spreadsheet-5000-rows.csv")
OUTPUT_FILE = "output.csv"

HOME_DIR = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")

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
def simple_workflow():
  @task()
  def logger():
    print("Dags running")
  
  download_data = BashOperator(
    task_id="download_task",
    bash_command=f"curl -sSL {DATA_URL} > {HOME_DIR}/{OUTPUT_FILE}"
  )

  local2gcs = LocalFilesystemToGCSOperator(
    src=f"{HOME_DIR}/{OUTPUT_FILE}",
    dst="/sample/",
    bucket=f"{BUCKET_NAME}",
    task_id="local2gcs",
    gcp_conn_id="google_cloud_default"
  )

  logger() >> download_data >> local2gcs

workflow = simple_workflow()