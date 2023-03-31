import click

from utils.extract_reg import extract_efw_reg


@click.command()
@click.option('--file', prompt='EWF file location', help='The EWF file to parse.')
def extract_ewf(file: str):
    extract_efw_reg(file)