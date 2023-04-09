import click

from cmds.cat_ewf import cat_ewf
from cmds.extract_ewf import extract_ewf
from cmds.ls_ewf import ls_ewf
from cmds.partition_ewf import partition_ewf


@click.group()
def cli():
    pass


cli.add_command(extract_ewf)
cli.add_command(cat_ewf)
cli.add_command(ls_ewf)
cli.add_command(partition_ewf)

if __name__ == '__main__':
    cli()
