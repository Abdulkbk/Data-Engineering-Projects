import os
import pandas as pd
import argparse
from sqlalchemy import create_engine

def main(params):
  user = params.user
  password = params.password
  host = params.host
  port = params.port
  db = params.db
  url = params.url
  table_name = params.table_name

  file_output = 'output.parquet'

  file_csv = 'output_data.csv'

  """Downloading the parquet file"""
  os.system(f'curl {url} -o {file_output}')

  """Creating an engine connection to postgresql database"""
  engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

  df_parquet = pd.read_parquet(f'{file_output}')

  df_parquet.to_csv(f'{file_csv}', index=False, sep="\t")

  df_iter = pd.read_csv(f'{file_csv}', iterator=True, chunksize=100000)

  df = next(df_iter)

  df.head(0).to_sql(name='yellow_taxi', con=engine, if_exists='replace')

  df.to_sql(name=f'{table_name}', con=engine, if_exists='append')

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="Ingest parquet file to postgres db running on docker")

  parser.add_argument('--user', help='username for db')
  parser.add_argument('--password', help='password for db')
  parser.add_argument('--host', help='host for db')
  parser.add_argument('--port', help='port for db')
  parser.add_argument('--db', help='db name')
  parser.add_argument('--table-name', help='table name')
  parser.add_argument('--url', help='url of the csv file')

  args = parser.parse_args()

  main(args)


