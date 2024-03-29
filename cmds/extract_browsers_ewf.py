from datetime import datetime
import time

import click
import pyewf
import pytsk3

from utils.constants import load_constants
from utils.extract_browsers import extract_browsers
from utils.extract_reg import EwfImgInfo
from utils.file import check_dir_exist
from utils.merkle import create_merkle_tree


@click.command('browsers')
@click.option('--file', prompt='EWF file location', help='The EWF file to parse.')
@click.option('--dest', default=f'./outputs/{datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y--%H-%M-%S")}', help='The destination directory.')
@click.option('--config', default='./config/default.yml', help='The config for data extraction.')
def extract_browsers_ewf(file: str, dest: str, config: str):
    print(f"Config file: {config}")
    CONFIG = load_constants(config)

    print(f"Destination folder: {dest}")
    check_dir_exist(dest)
    filenames = pyewf.glob(file)
    ewf_handle = pyewf.handle()
    ewf_handle.open(filenames)

    imageHandle = EwfImgInfo(ewf_handle)
    partitionTable = pytsk3.Volume_Info(imageHandle)

    for partition in partitionTable:
        if CONFIG['DATA_PARTITION'] == partition.desc:
            data_partition_fs = pytsk3.FS_Info(imageHandle, offset=(partition.start * 512))
            extract_browsers(data_partition_fs, f"{dest}/Browsers")

    merkle_proof = create_merkle_tree(dest)
    with open("merkle-proof.txt", 'w') as p:
        p.write(merkle_proof)
    print(f"Proof for extracted artifacts: {merkle_proof} written at ./merkle-proof.txt")
