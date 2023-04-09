import click

from utils.merkle import create_merkle_tree


@click.command('verify')
@click.option('--directory', prompt='Directory to check', help='The directory to verify.')
@click.option('--proof', prompt='Merkle proof hash', help='The merkle proof hash.')
def verify_merkle_proof(directory: str, proof: str):
    merkle_proof = create_merkle_tree(directory)
    if proof != merkle_proof:
        print(f"!! Invalid proof {merkle_proof} !!")
    else:
        print(f"The proof is correct {merkle_proof}")