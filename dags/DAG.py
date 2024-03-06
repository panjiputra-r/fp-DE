from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime, timedelta
from sqlalchemy import create_engine #koneksi ke postgres
import pandas as pd

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
 

from step.load import load_csv_to_postgres 
from step.fetch import fetch_data
from step.cleaning import preprocessing
from step.load_clean import load_csv_clean_to_postgres
from step.push import upload_to_elasticsearch


# memberi nama dan set waktu di waktu indonesia bagian barat        
default_args = {
    'owner': 'Panji', 
    'start_date': datetime(2024, 2, 22, 18, 00) - timedelta(hours=7)
}

with DAG(
    "final_project", #atur sesuai nama project kalian
    description='final',
    schedule_interval='30 06 * * 1', #atur schedule untuk menjalankan airflow pada 10:30 tiap hari senin.
    default_args=default_args, 
    catchup=False
) as dag:
    # Task : 1
    load_csv_task = PythonOperator(
        task_id='load_csv_to_postgres',
        python_callable=load_csv_to_postgres) #sesuai dengan nama fungsi yang dibuat
    
    #task: 2
    ''' Fungsi untuk mengambil data'''
    ambil_data_pg = PythonOperator(
        task_id='ambil_data_postgres',
        python_callable=fetch_data) #
    

    # Task: 3
    '''  Fungsi ini ditujukan untuk menjalankan pembersihan data.'''
    edit_data = PythonOperator(
        task_id='edit_data',
        python_callable=preprocessing)

    # Task : 4
    load_csv_clean_task = PythonOperator(
        task_id='load_csv_clean_to_postgres',
        python_callable=load_csv_clean_to_postgres)
    
    # Task: 5
    '''  Fungsi ini ditujukan untuk upload data ke elasticsearch.'''
    upload_data = PythonOperator(
        task_id='upload_data_elastic',
        python_callable=upload_to_elasticsearch)

    #proses untuk menjalankan di airflow
    load_csv_task >> ambil_data_pg >> edit_data >> load_csv_clean_task >> upload_data