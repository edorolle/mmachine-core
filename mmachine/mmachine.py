import shutil
import pkg_resources
import subprocess
import sys
from mmachine.mmachine_init import init
from mmachine.art import art

def main():
    
    print("Welcome to MysteryMachine! Version 0.0.2")

    if len(sys.argv)<2:
        print("List of commands: ")
        print("\n init: set up a new project folder\n dbt: create a new dbt project\n close: take down the docker containers")

    else:

        print("List of argument strings: %s" % sys.argv[1:])

        arg1 = sys.argv[1]
        if arg1 == "init":
            
            art()

            Docker_compose = pkg_resources.resource_filename('mmachine', 'data/docker-compose.yaml')

            shutil.copy(Docker_compose, './docker-compose.yaml')
            Dockerfile = pkg_resources.resource_filename('mmachine', 'data/Dockerfile')

            shutil.copy(Dockerfile, './Dockerfile')
            
            # script= pkg_resources.resource_filename('mmachine','script/shell_commands.sh')
            # print(script)

            subprocess.run('echo AIRFLOW_UID=50000 > .env',shell=True)
            subprocess.run(['echo',"AIRFLOW_GID=0", '>>', '.env'],shell=True)
            # subprocess.run("bash.exe "+script+" env", shell =True)
            
            init()
            
            subprocess.run(["docker", "compose","exec", "airflow-scheduler", "bash", "-c", r"cd ../dbt;printf 'template1\n1\n'|dbt init;mv /home/airflow/.dbt/profiles.yml /opt/dbt"], shell=True)
            # subprocess.run("bash.exe "+script+" dbt", shell =True)
            print("dbt folder correctly set up. ")

            print("Your project environment has been set up correctly!")
            
            FirstDag = pkg_resources.resource_filename('mmachine', 'script/template_dag.py')
            shutil.copy(FirstDag, './dags/template_dag.py')

            print("Everything went smoothly!")
            subprocess.run("docker ps", shell = True)
            print("Your docker Airflow instance is up and running at localhost:8080")
            print("Airflow Username: mmachine Password: mmachine")
        
        elif arg1 == "dbt":

            print("setting up a new dbt project...")
            subprocess.run("""docker compose exec -it airflow-scheduler bash -c "cd ../dbt;dbt init """, shell = True)
        elif arg1 == "close":

            print("Closing docker-compose...")
            subprocess.run("docker-compose down", shell = True)
            print("Done")