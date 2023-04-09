import pytsk3

from utils.constants import load_constants
from utils.file import check_dir_exist, copy_fs


def dump_edge(data_partition_fs, dest: str):
    check_dir_exist(dest)
    CONFIG = load_constants()
    hive_dir_object = data_partition_fs.open_dir(CONFIG['USERS_DIR_PATH'])

    for entry in hive_dir_object:
        if entry.info.name.name.decode() in [".", ".."]:
            continue
        elif entry.info.name.type == pytsk3.TSK_FS_NAME_TYPE_DIR:
            # AppData
            try:
                appdata_local_dir_object = data_partition_fs.open_dir(f"{CONFIG['USERS_DIR_PATH']}/{entry.info.name.name.decode()}/AppData/Local/Packages")
                for package_entry in appdata_local_dir_object:
                    if CONFIG['EDGE_PREFIX'] in package_entry.info.name.name.decode():
                        filepath = f"{CONFIG['USERS_DIR_PATH']}/{entry.info.name.name.decode()}/AppData/Local/Packages/{package_entry.info.name.name.decode()}"
                        print(f"Extracting {filepath} directory")
                        root_dir = data_partition_fs.open_dir(filepath)
                        copy_fs(data_partition_fs, root_dir, f"{dest}/Local/{entry.info.name.name.decode()}/{package_entry.info.name.name.decode()}", filepath)
            except:
                continue
            # WebCache
            try:
                filepath = f"{CONFIG['USERS_DIR_PATH']}/{entry.info.name.name.decode()}/AppData/Local/Microsoft/Windows/WebCache"
                root_dir = data_partition_fs.open_dir(filepath)
                print(f"Extracting {filepath} directory")
                copy_fs(data_partition_fs, root_dir, f"{dest}/Local/{entry.info.name.name.decode()}/WebCache", filepath)
            except:
                continue


# TODO: test
def dump_chrome(data_partition_fs, dest: str):
    check_dir_exist(dest)
    CONFIG = load_constants()
    hive_dir_object = data_partition_fs.open_dir(CONFIG['USERS_DIR_PATH'])

    for entry in hive_dir_object:
        if entry.info.name.name.decode() in [".", ".."]:
            continue
        elif entry.info.name.type == pytsk3.TSK_FS_NAME_TYPE_DIR:
            # AppData
            try:
                appdata_local_dir_object = data_partition_fs.open_dir(f"{CONFIG['USERS_DIR_PATH']}/{entry.info.name.name.decode()}/AppData/Local/Google")
                for package_entry in appdata_local_dir_object:
                    if CONFIG['CHROME_PREFIX'] in package_entry.info.name.name.decode():
                        filepath = f"{CONFIG['USERS_DIR_PATH']}/{entry.info.name.name.decode()}/AppData/Local/Packages/{package_entry.info.name.name.decode()}"
                        print(f"Extracting {filepath} directory")
                        root_dir = data_partition_fs.open_dir(filepath)
                        copy_fs(data_partition_fs, root_dir, f"{dest}/Local/{entry.info.name.name.decode()}/{package_entry.info.name.name.decode()}", filepath)
            except:
                continue


def dump_internet_explorer(data_partition_fs, dest: str):
    check_dir_exist(dest)
    CONFIG = load_constants()
    hive_dir_object = data_partition_fs.open_dir(CONFIG['USERS_DIR_PATH'])

    for entry in hive_dir_object:
        if entry.info.name.name.decode() in [".", ".."]:
            continue
        elif entry.info.name.type == pytsk3.TSK_FS_NAME_TYPE_DIR:
            # AppData Local
            try:
                appdata_local_dir_object = data_partition_fs.open_dir(f"{CONFIG['USERS_DIR_PATH']}/{entry.info.name.name.decode()}/AppData/Local/Microsoft/Windows")
                for package_entry in appdata_local_dir_object:
                    if package_entry.info.name.name.decode() in CONFIG["IE_PREFIXES"]:
                        filepath = f"{CONFIG['USERS_DIR_PATH']}/{entry.info.name.name.decode()}/AppData/Local/Microsoft/Windows/{package_entry.info.name.name.decode()}"
                        print(f"Extracting {filepath} directory")
                        root_dir = data_partition_fs.open_dir(filepath)
                        copy_fs(data_partition_fs, root_dir, f"{dest}/Local/{entry.info.name.name.decode()}/{package_entry.info.name.name.decode()}", filepath)
            except:
                continue
            # IE AppData Roaming
            try:
                appdata_local_dir_object = data_partition_fs.open_dir(f"{CONFIG['USERS_DIR_PATH']}/{entry.info.name.name.decode()}/AppData/Roaming/Microsoft/Internet Explorer")
                for package_entry in appdata_local_dir_object:
                    if package_entry.info.name.name.decode() in CONFIG["IE_PREFIXES"]:
                        filepath = f"{CONFIG['USERS_DIR_PATH']}/{entry.info.name.name.decode()}/AppData/Roaming/Microsoft/Internet Explorer/{package_entry.info.name.name.decode()}"
                        print(f"Extracting {filepath} directory")
                        root_dir = data_partition_fs.open_dir(filepath)
                        copy_fs(data_partition_fs, root_dir, f"{dest}/Roaming/{entry.info.name.name.decode()}/{package_entry.info.name.name.decode()}", filepath)
            except:
                continue
            # Windows AppData Roaming
            try:
                appdata_local_dir_object = data_partition_fs.open_dir(f"{CONFIG['USERS_DIR_PATH']}/{entry.info.name.name.decode()}/AppData/Roaming/Microsoft/Windows")
                for package_entry in appdata_local_dir_object:
                    if package_entry.info.name.name.decode() in CONFIG["IE_PREFIXES"]:
                        filepath = f"{CONFIG['USERS_DIR_PATH']}/{entry.info.name.name.decode()}/AppData/Roaming/Microsoft/Windows/{package_entry.info.name.name.decode()}"
                        print(f"Extracting {filepath} directory")
                        root_dir = data_partition_fs.open_dir(filepath)
                        copy_fs(data_partition_fs, root_dir, f"{dest}/Roaming/{entry.info.name.name.decode()}/{package_entry.info.name.name.decode()}", filepath)
            except:
                continue


# TODO: Firefox
def extract_browsers(data_partition_fs, dest: str):
    check_dir_exist(dest)
    dump_edge(data_partition_fs, f"{dest}/Edge")
    dump_chrome(data_partition_fs, f"{dest}/Google")
    dump_internet_explorer(data_partition_fs, f"{dest}/IE")
