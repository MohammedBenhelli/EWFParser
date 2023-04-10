import click

from cmds.cat_ewf import cat_ewf
from cmds.cp_ewf import cp_ewf
from cmds.extract_browsers_ewf import extract_browsers_ewf
from cmds.extract_ewf import extract_ewf
from cmds.extract_hives_ewf import extract_hives_ewf
from cmds.extract_logs_ewf import extract_logs_ewf
from cmds.extract_reg_ewf import extract_reg_ewf
from cmds.ls_ewf import ls_ewf
from cmds.partition_ewf import partition_ewf
from cmds.verify_merkle_proof import verify_merkle_proof


@click.group()
def cli():
    pass


cli.add_command(extract_ewf)
cli.add_command(extract_browsers_ewf)
cli.add_command(extract_logs_ewf)
cli.add_command(extract_hives_ewf)
cli.add_command(extract_reg_ewf)
cli.add_command(cat_ewf)
cli.add_command(cp_ewf)
cli.add_command(ls_ewf)
cli.add_command(partition_ewf)
cli.add_command(verify_merkle_proof)

if __name__ == '__main__':
    cli()
