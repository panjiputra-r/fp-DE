import pandas as pd

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

def upload_to_elasticsearch():
    # mengupload data ke elasticsearch
    es = Elasticsearch("http://elasticsearch:9200")
    df = pd.read_csv("/opt/airflow/dags/bank-additional-full_clean.csv")
    
    for i, r in df.iterrows():
        doc = r.to_dict()  # Convert the row to a dictionary
        res = es.index(index="table_finalproject", id=i+1, body=doc)
        print(f"Response from Elasticsearch: {res}")