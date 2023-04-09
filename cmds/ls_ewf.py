import click
import pyewf
import pytsk3

from utils.extract_reg import EwfImgInfo
from utils.file import filetype_enum_to_str


@click.command('ls')
@click.option('--file', prompt='EWF file location', help='The EWF file to parse.')
@click.argument('target', default="/")
def ls_ewf(file: str, target: str):
    filenames = pyewf.glob(file)
    ewf_handle = pyewf.handle()
    ewf_handle.open(filenames)

    imageHandle = EwfImgInfo(ewf_handle)
    partitionTable = pytsk3.Volume_Info(imageHandle)

    for partition in partitionTable:
        if b'Basic data partition' == partition.desc:
            data_partition_fs = pytsk3.FS_Info(imageHandle, offset=(partition.start * 512))
            target_dir_object = data_partition_fs.open_dir(target)
            for entry in target_dir_object:
                print(f"{entry.info.name.name.decode()}\ttype: {filetype_enum_to_str(entry.info.name.type)}")