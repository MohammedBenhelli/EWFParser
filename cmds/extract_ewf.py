from datetime import datetime
import time

import click
import pyewf
import pytsk3

from utils.constants import DATA_PARTITION, CONFIG_DIR_PATH, USERS_DIR_PATH
from utils.extract_reg import extract_efw_reg, EwfImgInfo, extract_efw_hive
from utils.file import check_dir_exist


@click.command()
@click.option('--file', prompt='EWF file location', help='The EWF file to parse.')
@click.option('--dest', default=f'outputs/{datetime.fromtimestamp(time.time()).strftime("%d-%m-%Y--%H-%M-%S")}',
              help='The destination directory.')
def extract_ewf(file: str, dest: str):
    print(f"Destination folder: {dest}")
    check_dir_exist(dest)
    filenames = pyewf.glob(file)
    ewf_handle = pyewf.handle()
    ewf_handle.open(filenames)

    imageHandle = EwfImgInfo(ewf_handle)

    partitionTable = pytsk3.Volume_Info(imageHandle)

    for partition in partitionTable:
        print(f"Found {partition.desc} partition")
        if DATA_PARTITION == partition.desc:
            data_partition_fs = pytsk3.FS_Info(imageHandle, offset=(partition.start * 512))
            # System reg
            config_dir_object = data_partition_fs.open_dir(CONFIG_DIR_PATH)
            extract_efw_reg(config_dir_object, data_partition_fs, dest)
            # Users hives
            hive_dir_object = data_partition_fs.open_dir(USERS_DIR_PATH)
            extract_efw_hive(hive_dir_object, data_partition_fs, dest)
