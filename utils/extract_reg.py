from datetime import datetime

import pyewf
import pytsk3


class EwfImgInfo(pytsk3.Img_Info):
    def __init__(self, ewf_handle: pyewf.handle):
        self._ewf_handle = ewf_handle
        super(EwfImgInfo, self).__init__()

    def close(self):
        self._ewf_handle.close()

    #! WARNING: Dogshit method
    def read(self, offset: int, size: int):
        self._ewf_handle.seek(offset)
        return self._ewf_handle.read(size)

    def get_size(self):
        return self._ewf_handle.get_media_size()


#TODO: les fichiers du registre système et les ruches utilisateur
def extract_efw_reg(efw_file_path: str):
    filenames = pyewf.glob(efw_file_path)
    ewf_handle = pyewf.handle()
    ewf_handle.open(filenames)

    imageHandle = EwfImgInfo(ewf_handle)

    partitionTable = pytsk3.Volume_Info(imageHandle)

    for partition in partitionTable:
        print(partition.addr, partition.desc, "%ss(%s)" % (partition.start, partition.start * 512), partition.len)
        if 'NTFS' in partition.desc:
            filesystemObject = pytsk3.FS_Info(imageHandle, offset=(partition.start*512))
            fileobject = filesystemObject.open("/$MFT")
            print("File Inode:",fileobject.info.meta.addr)
            print("File Name:",fileobject.info.name.name)
            print( "File Creation Time:",datetime.fromtimestamp(fileobject.info.meta.crtime).strftime('%Y-%m-%d %H:%M:%S'))
            outFileName = str(partition.addr)+fileobject.info.name.name
            print(outFileName)
            outfile = open(outFileName, 'w')
            filedata = fileobject.read_random(0,fileobject.info.meta.size)
            outfile.write(filedata)
            outfile.close()
