import pytsk3

from utils.constants import load_constants
from utils.file import check_dir_exist, copy_fs


def dump_protect_web_cache(data_partition_fs, dest: str):
    check_dir_exist(dest)
    CONFIG = load_constants()
    hive_dir_object = data_partition_fs.open_dir(CONFIG['USERS_DIR_PATH'])
    print("Searching for Protect and WebCache artifacts")

    for entry in hive_dir_object:
        if entry.info.name.name.decode() in [".", ".."]:
            continue
        elif entry.info.name.type == pytsk3.TSK_FS_NAME_TYPE_DIR:
            # WebCache
            try:
                filepath = f"{CONFIG['USERS_DIR_PATH']}/{entry.info.name.name.decode()}/AppData/Local/Microsoft/Windows/WebCache"
                root_dir = data_partition_fs.open_dir(filepath)
                print(f"Extracting {filepath} directory")
                copy_fs(data_partition_fs, root_dir, f"{dest}/Local/{entry.info.name.name.decode()}/WebCache", filepath)
            except Exception:
                continue
            # Protect
            try:
                filepath = f"{CONFIG['USERS_DIR_PATH']}/{entry.info.name.name.decode()}/AppData/Local/Microsoft/Protect"
                root_dir = data_partition_fs.open_dir(filepath)
                print(f"Extracting {filepath} directory")
                copy_fs(data_partition_fs, root_dir, f"{dest}/Local/{entry.info.name.name.decode()}/Protect", filepath)
            except Exception:
                continue


def dump_edge(data_partition_fs, dest: str):
    check_dir_exist(dest)
    CONFIG = load_constants()
    hive_dir_object = data_partition_fs.open_dir(CONFIG['USERS_DIR_PATH'])
    print("Searching for Edge artifacts")

    for entry in hive_dir_object:
        if entry.info.name.name.decode() in [".", ".."]:
            continue
        elif entry.info.name.type == pytsk3.TSK_FS_NAME_TYPE_DIR:
            # AppData
            try:
                appdata_local_dir_object = data_partition_fs.open_dir(
                    f"{CONFIG['USERS_DIR_PATH']}/{entry.info.name.name.decode()}/AppData/Local/Packages")
                for package_entry in appdata_local_dir_object:
                    if CONFIG['EDGE_PREFIX'] in package_entry.info.name.name.decode():
                        filepath = f"{CONFIG['USERS_DIR_PATH']}/{entry.info.name.name.decode()}/AppData/Local/Packages/{package_entry.info.name.name.decode()}"
                        print(f"Extracting {filepath} directory")
                        root_dir = data_partition_fs.open_dir(filepath)
                        copy_fs(data_partition_fs, root_dir,
                                f"{dest}/Local/{entry.info.name.name.decode()}/{package_entry.info.name.name.decode()}",
                                filepath)
            except Exception:
                continue
            # Edge Chromium
            try:
                filepath = f"{CONFIG['USERS_DIR_PATH']}/{entry.info.name.name.decode()}/AppData/Local/Microsoft/Edge"
                root_dir = data_partition_fs.open_dir(filepath)
                print(f"Extracting {filepath} directory")
                copy_fs(data_partition_fs, root_dir, f"{dest}/Local/{entry.info.name.name.decode()}/EdgeChromium",
                        filepath)
            except Exception:
                continue


def dump_chrome(data_partition_fs, dest: str):
    check_dir_exist(dest)
    CONFIG = load_constants()
    hive_dir_object = data_partition_fs.open_dir(CONFIG['USERS_DIR_PATH'])
    print("Searching for Chrome artifacts")

    for entry in hive_dir_object:
        if entry.info.name.name.decode() in [".", ".."]:
            continue
        elif entry.info.name.type == pytsk3.TSK_FS_NAME_TYPE_DIR:
            # AppData
            try:
                appdata_local_dir_object = data_partition_fs.open_dir(
                    f"{CONFIG['USERS_DIR_PATH']}/{entry.info.name.name.decode()}/AppData/Local/Google")
                for package_entry in appdata_local_dir_object:
                    if CONFIG['CHROME_PREFIX'] in package_entry.info.name.name.decode():
                        filepath = f"{CONFIG['USERS_DIR_PATH']}/{entry.info.name.name.decode()}/AppData/Local/Google/{package_entry.info.name.name.decode()}"
                        print(f"Extracting {filepath} directory")
                        root_dir = data_partition_fs.open_dir(filepath)
                        copy_fs(data_partition_fs, root_dir,
                                f"{dest}/Local/{entry.info.name.name.decode()}/{package_entry.info.name.name.decode()}",
                                filepath)
            except Exception:
                continue


def dump_internet_explorer(data_partition_fs, dest: str):
    check_dir_exist(dest)
    CONFIG = load_constants()
    hive_dir_object = data_partition_fs.open_dir(CONFIG['USERS_DIR_PATH'])
    print("Searching for Internet Explorer artifacts")

    for entry in hive_dir_object:
        if entry.info.name.name.decode() in [".", ".."]:
            continue
        elif entry.info.name.type == pytsk3.TSK_FS_NAME_TYPE_DIR:
            # AppData Local
            try:
                appdata_local_dir_object = data_partition_fs.open_dir(
                    f"{CONFIG['USERS_DIR_PATH']}/{entry.info.name.name.decode()}/AppData/Local/Microsoft/Windows")
                for package_entry in appdata_local_dir_object:
                    if package_entry.info.name.name.decode() in CONFIG["IE_PREFIXES"]:
                        filepath = f"{CONFIG['USERS_DIR_PATH']}/{entry.info.name.name.decode()}/AppData/Local/Microsoft/Windows/{package_entry.info.name.name.decode()}"
                        print(f"Extracting {filepath} directory")
                        root_dir = data_partition_fs.open_dir(filepath)
                        copy_fs(data_partition_fs, root_dir,
                                f"{dest}/Local/{entry.info.name.name.decode()}/{package_entry.info.name.name.decode()}",
                                filepath)
            except Exception:
                continue
            # IE AppData Roaming
            try:
                filepath = f"{CONFIG['USERS_DIR_PATH']}/{entry.info.name.name.decode()}/AppData/Roaming/Microsoft/Internet Explorer"
                root_dir = data_partition_fs.open_dir(filepath)
                print(f"Extracting {filepath} directory")
                copy_fs(data_partition_fs, root_dir,
                        f"{dest}/Roaming/{entry.info.name.name.decode()}/Internet Explorer", filepath)
            except Exception:
                continue
            # Windows AppData Roaming
            try:
                appdata_local_dir_object = data_partition_fs.open_dir(
                    f"{CONFIG['USERS_DIR_PATH']}/{entry.info.name.name.decode()}/AppData/Roaming/Microsoft/Windows")
                for package_entry in appdata_local_dir_object:
                    if package_entry.info.name.name.decode() in CONFIG["IE_PREFIXES"]:
                        filepath = f"{CONFIG['USERS_DIR_PATH']}/{entry.info.name.name.decode()}/AppData/Roaming/Microsoft/Windows/{package_entry.info.name.name.decode()}"
                        print(f"Extracting {filepath} directory")
                        root_dir = data_partition_fs.open_dir(filepath)
                        copy_fs(data_partition_fs, root_dir,
                                f"{dest}/Roaming/{entry.info.name.name.decode()}/{package_entry.info.name.name.decode()}",
                                filepath)
            except Exception:
                continue
            # Office
            try:
                filepath = f"{CONFIG['USERS_DIR_PATH']}/{entry.info.name.name.decode()}/AppData/Roaming/Microsoft/Office"
                root_dir = data_partition_fs.open_dir(filepath)
                print(f"Extracting {filepath} directory")
                copy_fs(data_partition_fs, root_dir, f"{dest}/Roaming/{entry.info.name.name.decode()}/Office", filepath)
            except Exception:
                continue


def dump_firefox(data_partition_fs, dest: str):
    check_dir_exist(dest)
    CONFIG = load_constants()
    hive_dir_object = data_partition_fs.open_dir(CONFIG['USERS_DIR_PATH'])
    print("Searching for Firefox artifacts")

    for entry in hive_dir_object:
        if entry.info.name.name.decode() in [".", ".."]:
            continue
        elif entry.info.name.type == pytsk3.TSK_FS_NAME_TYPE_DIR:
            # AppData
            try:
                appdata_local_dir_object = data_partition_fs.open_dir(
                    f"{CONFIG['USERS_DIR_PATH']}/{entry.info.name.name.decode()}/AppData/Roaming/Mozilla")
                for package_entry in appdata_local_dir_object:
                    if CONFIG['FIREFOX_PREFIX'] in package_entry.info.name.name.decode():
                        filepath = f"{CONFIG['USERS_DIR_PATH']}/{entry.info.name.name.decode()}/AppData/Roaming/Mozilla/{package_entry.info.name.name.decode()}"
                        print(f"Extracting {filepath} directory")
                        root_dir = data_partition_fs.open_dir(filepath)
                        copy_fs(data_partition_fs, root_dir,
                                f"{dest}/Roaming/{entry.info.name.name.decode()}/{package_entry.info.name.name.decode()}",
                                filepath)
            except Exception:
                continue


def dump_brave(data_partition_fs, dest: str):
    check_dir_exist(dest)
    CONFIG = load_constants()
    hive_dir_object = data_partition_fs.open_dir(CONFIG['USERS_DIR_PATH'])
    print("Searching for Brave artifacts")

    for entry in hive_dir_object:
        if entry.info.name.name.decode() in [".", ".."]:
            continue
        elif entry.info.name.type == pytsk3.TSK_FS_NAME_TYPE_DIR:
            # AppData
            try:
                appdata_local_dir_object = data_partition_fs.open_dir(
                    f"{CONFIG['USERS_DIR_PATH']}/{entry.info.name.name.decode()}/AppData/Local/BraveSoftware/Brave-Browser")
                for package_entry in appdata_local_dir_object:
                    if package_entry.info.name.name.decode() in CONFIG['BRAVE_PREFIXES']:
                        filepath = f"{CONFIG['USERS_DIR_PATH']}/{entry.info.name.name.decode()}/AppData/Local/BraveSoftware/Brave-Browser/{package_entry.info.name.name.decode()}"
                        print(f"Extracting {filepath} directory")
                        root_dir = data_partition_fs.open_dir(filepath)
                        copy_fs(data_partition_fs, root_dir,
                                f"{dest}/Local/{entry.info.name.name.decode()}/{package_entry.info.name.name.decode()}",
                                filepath)
            except Exception:
                continue


def dump_opera(data_partition_fs, dest: str):
    check_dir_exist(dest)
    CONFIG = load_constants()
    hive_dir_object = data_partition_fs.open_dir(CONFIG['USERS_DIR_PATH'])
    print("Searching for Opera artifacts")

    for entry in hive_dir_object:
        if entry.info.name.name.decode() in [".", ".."]:
            continue
        elif entry.info.name.type == pytsk3.TSK_FS_NAME_TYPE_DIR:
            # Local Appdata
            try:
                filepath = f"{CONFIG['USERS_DIR_PATH']}/{entry.info.name.name.decode()}/AppData/Local/Opera Software/Opera Stable"
                root_dir = data_partition_fs.open_dir(filepath)
                print(f"Extracting {filepath} directory")
                copy_fs(data_partition_fs, root_dir, f"{dest}/Local/{entry.info.name.name.decode()}/Opera", filepath)
            except Exception:
                continue
            # Roaming Appdata
            try:
                filepath = f"{CONFIG['USERS_DIR_PATH']}/{entry.info.name.name.decode()}/AppData/Roaming/Opera Software/Opera Stable"
                root_dir = data_partition_fs.open_dir(filepath)
                print(f"Extracting {filepath} directory")
                copy_fs(data_partition_fs, root_dir, f"{dest}/Roaming/{entry.info.name.name.decode()}/Opera", filepath)
            except Exception:
                continue


def dump_puffin(data_partition_fs, dest: str):
    check_dir_exist(dest)
    CONFIG = load_constants()
    hive_dir_object = data_partition_fs.open_dir(CONFIG['USERS_DIR_PATH'])
    print("Searching for Puffin artifacts")

    for entry in hive_dir_object:
        if entry.info.name.name.decode() in [".", ".."]:
            continue
        elif entry.info.name.type == pytsk3.TSK_FS_NAME_TYPE_DIR:
            # Local Appdata
            try:
                filepath = f"{CONFIG['USERS_DIR_PATH']}/{entry.info.name.name.decode()}/AppData/Local/PuffinSecureBrowser"
                root_dir = data_partition_fs.open_dir(filepath)
                print(f"Extracting {filepath} directory")
                copy_fs(data_partition_fs, root_dir, f"{dest}/Local/{entry.info.name.name.decode()}/Puffin", filepath)
            except Exception:
                continue


def extract_browsers(data_partition_fs, dest: str):
    check_dir_exist(dest)
    dump_protect_web_cache(data_partition_fs, f"{dest}/ProtectWebCache")

    dump_brave(data_partition_fs, f"{dest}/Brave")
    dump_chrome(data_partition_fs, f"{dest}/Google")
    dump_edge(data_partition_fs, f"{dest}/Edge")
    dump_firefox(data_partition_fs, f"{dest}/Firefox")
    dump_internet_explorer(data_partition_fs, f"{dest}/IE")
    dump_opera(data_partition_fs, f"{dest}/Opera")
    dump_puffin(data_partition_fs, f"{dest}/Puffin")
