import subprocess as sp

def init():

    sp.run(" docker build . --tag mmachine:0.2 ", shell =True)
    sp.run(" echo Docker image successfully built ", shell =True)
    sp.run(" docker-compose up airflow-init  ", shell =True)
    sp.run(" docker-compose up -d ", shell =True)
    sp.run(" echo Launching docker compose... ", shell =True)


    
         
         
         
         
         
         
          
         