from prefect import flow, task
from prefect_shell import ShellOperation

DBT_DIR = "../poke_pg_dbt"


@task
def run_dbt(command: str):
    return ShellOperation(
        commands=[command],
        working_dir=DBT_DIR
    ).run()


@flow
def dbt_flow():
    run_dbt("dbt deps")
    run_dbt("dbt run -s operational_data")


if __name__ == "__main__":
    dbt_flow()