# **Data Pipeline - Extract Transform Load:**

**ETL**: Is a data ingestion technique whereby data is gotton from sources (usually a **datalake**), moved to a server for **Transformation**, and then store in **datawarehouse** usually in a structured format.

---

| File                   | Desc                                                                                |
| ---------------------- | ----------------------------------------------------------------------------------- |
| Scripts/ingest_data.py | _A python file that contains the loading, transformation, and ingestion script_     |
| docker-compose.yml     | _A docker-compose file that spins up Postgresql and pg4admin in a docker container_ |
| Dockerfile             | _Used to create an image of the whole pipeline_                                     |

---
