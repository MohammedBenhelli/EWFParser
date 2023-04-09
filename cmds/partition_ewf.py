import click
import pyewf
import pytsk3

from utils.extract_reg import EwfImgInfo


@click.command('partition')
@click.option('--file', prompt='EWF file location', help='The EWF file to parse.')
def partition_ewf(file: str):
    filenames = pyewf.glob(file)
    ewf_handle = pyewf.handle()
    ewf_handle.open(filenames)

    imageHandle = EwfImgInfo(ewf_handle)
    partitionTable = pytsk3.Volume_Info(imageHandle)

    for partition in partitionTable:
        print(f"{partition.desc.decode()}\tstart: {partition.start}\tlength: {partition.len}")