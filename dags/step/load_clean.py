# import libraries
from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from sqlalchemy import create_engine #koneksi ke postgres
import pandas as pd

def load_csv_clean_to_postgres():
    # meload data csv ke postgres
    database = "airflow_finalproject"
    username = "airflow_finalproject"
    password = "airflow_finalproject"
    host = "postgres"

    # Membuat URL koneksi PostgreSQL
    postgres_url = f"postgresql+psycopg2://{username}:{password}@{host}/{database}"

    # Gunakan URL ini saat membuat koneksi SQLAlchemy
    engine = create_engine(postgres_url)
    # engine= create_engine("postgresql+psycopg2://airflow:airflow@postgres/airflow")
    conn = engine.connect()

    df = pd.read_csv('/opt/airflow/dags/bank-additional-full_clean.csv')
    #df.to_sql(nama_table, conn, index=False, if_exists='replace')
    df.to_sql('table_finalproject_clean', conn, index=False, if_exists='replace')  # Menggunakan if_exists='replace' agar tabel digantikan jika sudah ada
    
