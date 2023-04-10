import click

from utils.merkle import create_merkle_tree


@click.command('get-proof')
@click.argument('directory', required=True)
def get_merkle_proof(directory: str):
    merkle_proof = create_merkle_tree(directory)
    print(f"Proof for {directory}: {merkle_proof}")