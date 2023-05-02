from datetime import datetime, timedelta
import psycopg2
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from includes.py_scripts.load import load
from includes.py_scripts.trans_data import trans_data
from includes.py_scripts.extract_data import extract_data


default_args = {
    'owner': 'Mohammad Ashikur Rahman',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}


with DAG(
    dag_id='collision_data_analysis',
    default_args=default_args,
    start_date=datetime(2023, 5, 1),
    schedule_interval='10 0 * * *'
) as dag:

    load_task = PythonOperator(task_id='load', python_callable=load)

    trans_task = PythonOperator(task_id='trans_data', python_callable=trans_data)

    extract_task = PythonOperator(task_id='extract_data', python_callable=extract_data)

    load_task >> trans_task >> extract_task