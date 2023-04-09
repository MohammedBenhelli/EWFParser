import click
import pyewf
import pytsk3

from utils.extract_reg import EwfImgInfo
from utils.file import filetype_enum_to_str


@click.command('cat')
@click.option('--file', prompt='EWF file location', help='The EWF file to parse.')
@click.argument('target', default="/")
def cat_ewf(file: str, target: str):
    filenames = pyewf.glob(file)
    ewf_handle = pyewf.handle()
    ewf_handle.open(filenames)

    imageHandle = EwfImgInfo(ewf_handle)
    partitionTable = pytsk3.Volume_Info(imageHandle)

    for partition in partitionTable:
        if b'Basic data partition' == partition.desc:
            data_partition_fs = pytsk3.FS_Info(imageHandle, offset=(partition.start * 512))
            fileobject = data_partition_fs.open(target)
            if fileobject.info.meta.size > 0:
                print(fileobject.read_random(0, fileobject.info.meta.size))
