from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

#for testing a simple DAG in Airflow

with DAG(
    dag_id="test_dag",
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:
    t1 = EmptyOperator(task_id="dummy")