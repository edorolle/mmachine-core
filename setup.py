from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
     name='mmachine',  
     version='0.0.4',
     entry_points = {
        "console_scripts": ['mmachine = mmachine.mmachine:main']
        },
     packages = ["mmachine"],
     author="Edoardo Rolle",
     author_email="edoardo.mmachine@gmail.com",
     description="A tool to setup a data engineering environment with Airflow and DBT ready",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/DE-Edo/mmachine-core",
     download_url = "https://github.com/DE-Edo/mmachine-core/archive/refs/tags/0.0.4.tar.gz",
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     package_data={'mmachine': ['data/Dockerfile','data/docker-compose.yaml','script/shell_commands.sh',
     'script/template_dag.py']},
 )