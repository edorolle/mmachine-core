# !/bin/bash

#This is deprecated for compatibility reasons

case $1 in
    env)
        echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env
        exit;;
    dbt)
        docker compose exec airflow-scheduler bash -c "cd ../dbt;printf 'template1\n1\n' | dbt init;mv /home/airflow/.dbt/profiles.yml /opt/dbt"
        exit;;
    esac
