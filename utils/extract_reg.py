import pyewf
import pytsk3

from utils.Registry import Registry
from utils.constants import CONFIG_DIR_PATH, REG_FILES, USER_HIVES, USERS_DIR_PATH
from utils.file import check_dir_exist, to_windows_path


class EwfImgInfo(pytsk3.Img_Info):
    def __init__(self, ewf_handle: pyewf.handle):
        self._ewf_handle = ewf_handle
        super(EwfImgInfo, self).__init__()

    def close(self):
        self._ewf_handle.close()

    def read(self, offset: int, size: int):
        self._ewf_handle.seek(offset)
        return self._ewf_handle.read(size)

    def get_size(self):
        return self._ewf_handle.get_media_size()


def extract_all_reg(key, dest: str):
    check_dir_exist(f"{dest}/" + to_windows_path(key.path()))
    for v in key.values():
        if '/' in to_windows_path(v.name()):
            check_dir_exist(
                f"{dest}/" + to_windows_path(key.path()) + '/' + '/'.join(to_windows_path(v.name()).split('/')[0:-1]))
        with open(f"{dest}/" + to_windows_path(key.path()) + f"/{to_windows_path(v.name())}.json", "w") as f:
            f.write(v.JSON())
    for sub_key in key.subkeys():
        extract_all_reg(sub_key, dest)


def extract_efw_reg(config_dir_object, data_partition_fs, dest: str):
    for entry in config_dir_object:
        if entry.info.name.name.decode() in REG_FILES:
            filepath = CONFIG_DIR_PATH + "/" + entry.info.name.name.decode()
            print(f"Extracting {filepath} registry")
            fileobject = data_partition_fs.open(filepath)
            with open(f"{dest}/{fileobject.info.name.name.decode()}", 'wb') as f:
                f.write(fileobject.read_random(0, fileobject.info.meta.size))
            reg = Registry(f"{dest}/{fileobject.info.name.name.decode()}")
            extract_all_reg(reg.root(), f"{dest}/{entry.info.name.name.decode()}_extract")


def extract_efw_hive(config_dir_object, data_partition_fs, dest: str):
    for entry in config_dir_object:
        if entry.info.name.name.decode() in [".", ".."]:
            continue
        if entry.info.name.type == pytsk3.TSK_FS_NAME_TYPE_DIR:
            subdir = entry.as_directory()
            for user_entry in subdir:
                if user_entry.info.name.name.decode() in USER_HIVES:
                    filepath = USERS_DIR_PATH + "/" + entry.info.name.name.decode() + "/" + user_entry.info.name.name.decode()
                    print(f"Extracting {filepath} registry")
                    fileobject = data_partition_fs.open(filepath)
                    with open(f"{dest}/{fileobject.info.name.name.decode()}", 'wb') as f:
                        f.write(fileobject.read_random(0, fileobject.info.meta.size))
                    reg = Registry(f"{dest}/{fileobject.info.name.name.decode()}")
                    extract_all_reg(reg.root(),
                                    f"{dest}/{entry.info.name.name.decode()}/{user_entry.info.name.name.decode()}_extract")
