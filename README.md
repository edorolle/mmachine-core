# MysteryMachine
Welcome to mmachine! 

Mystery Machine is a tool that allows users to build a full data engineering project environment
just by writing one line of code.

![Example project directory created](./example_dir.png)


It works by launching airflow on docker-compose and sets up a dbt project while smoothly moving dependencies.

## Quickstart

### Installation

Right now mmachine is on test mode and can be installed via PyPitest:

`
pip install -i https://test.pypi.org/simple/ mmachine
`

## Commands

The current version of mmachine has 3 commands:

`
mmachine init
`
  create a new DE project environment in the directory you are currently in
`
mmachine dbt
`
  create a new Dbt Project
`
mmachine close
`
  closes your running docker-compose instances
