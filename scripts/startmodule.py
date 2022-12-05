import pathlib
import click

from .cli_tools.templates import schemas_template, endpoints_template


@click.command()
@click.argument('name')
def startmodule(name: str):
    """
    This command create module in src
    """
    path = pathlib.Path('.') / 'src' / 'api' / name
    path.mkdir(parents=True, exist_ok=True)
    
    schema_file = path / 'schemas.py'

    schema_file.write_text(schemas_template.substitute())

    endpoint_file = path / 'endpoints.py'

    endpoint_file.write_text(endpoints_template.substitute(app_name=name)) 