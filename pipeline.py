from dagster import job, op


@op
def get_name():
    return "dagster"


@op
def hello(name: str):
    print(f"Hello, {name}!")


@job(description="Hello world Dagster pipeline")
def hello_dagster():
    hello(get_name())