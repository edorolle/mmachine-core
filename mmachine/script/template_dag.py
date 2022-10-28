from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

## in order for this dag to run succesfully you must first set up the db connection in the dbt/profile.yml file

with DAG("MysteryMachine_Template_Dag", start_date=datetime(2022,10,25),
schedule_interval = None, catchup = False) as dag:

    task1 = BashOperator(
        task_id ="run_dbt",
        bash_command="cd /opt/dbt&&dbt run --project-dir template1 --profiles-dir ."
    )
