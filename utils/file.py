import os

import pytsk3


def check_dir_exist(d: str):
    if not os.path.isdir(d):
        # print(f"Creating {d} directory")
        os.makedirs(d)


def to_windows_path(p: str) -> str:
    return p.replace('\\', '/')\
        .replace('*', 'all')\
        .replace(':', '__')\
        .replace('?', 'in')\
        .replace('<', '__') \
        .replace('>', '__') \
        .replace('|', '__') \
        .replace('"', '__')

def filetype_enum_to_str(i: int) -> str:
    match i:
        case 0:
            return 'Unknown type'
        case 1:
            return 'Named pipe'
        case 2:
            return 'Character device'
        case 3:
            return 'Directory'
        case 4:
            return 'Block device'
        case 5:
            return 'Regular file'
        case 6:
            return 'Symbolic link'
        case 7:
            return 'Socket'
        case 8:
            return 'Shadow inode (solaris)'
        case 9:
            return 'Whiteout (openbsd)'
        case 10:
            return 'Special (TSK added "Virtual" files)'
        case 11:
            return 'Special (TSK added "Virtual" directories)'


def copy_fs(data_partition_fs, directory, dest: str, parent_path):
    check_dir_exist(to_windows_path(dest))
    for entry in directory:
        if entry.info.name.name.decode() in [".", ".."]:
            continue
        filepath = parent_path + "/" + entry.info.name.name.decode()
        if entry.info.name.type == pytsk3.TSK_FS_NAME_TYPE_DIR:
            subdir = entry.as_directory()
            copy_fs(data_partition_fs, subdir, f"{dest}/{entry.info.name.name.decode()}", filepath)
        else:
            fileobject = data_partition_fs.open(filepath)
            if fileobject.info.meta.size > 0:
                with open(to_windows_path(f"{dest}/{entry.info.name.name.decode()}"), 'wb') as f:
                    f.write(fileobject.read_random(0, fileobject.info.meta.size))
