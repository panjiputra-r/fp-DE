# import libraries
from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from sqlalchemy import create_engine #koneksi ke postgres
import pandas as pd

def fetch_data():
    # fetch data
    database = "airflow_finalproject"
    username = "airflow_finalproject"
    password = "airflow_finalproject"
    host = "postgres"

    # Membuat URL koneksi PostgreSQL
    postgres_url = f"postgresql+psycopg2://{username}:{password}@{host}/{database}"

    # Gunakan URL ini saat membuat koneksi SQLAlchemy
    engine = create_engine(postgres_url)
    conn = engine.connect()

    df = pd.read_sql_query("select * from table_finalproject", conn) 
    df.to_csv('/opt/airflow/dags/bank-additional-full_new.csv', sep=',', index=False)