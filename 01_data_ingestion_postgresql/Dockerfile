FROM python:latest

RUN apt install curl

WORKDIR /app

RUN pip install pandas sqlalchemy psycopg2 pyarrow

COPY ./Scripts/ingest_data.py ingest_data.py

ENTRYPOINT [ "python", "ingest_data.py" ]