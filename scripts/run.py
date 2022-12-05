import os
import click


@click.command()
@click.option('--host', 'host', default='127.0.0.1')
@click.option('--port', 'port', default=8000)
@click.option('--reload', 'reload', default=True)
def run_dev(host: str, port: int, reload: bool):
    """
    This command starts the application in development mode
    """
    os.system(f"uvicorn src.main:app --host {host} --port {port} {'--reload' if reload else ''}")
