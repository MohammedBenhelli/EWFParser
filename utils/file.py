import os


def check_dir_exist(d: str):
    if not os.path.isdir(d):
        # print(f"Creating {d} directory")
        os.makedirs(d)


def to_windows_path(p: str) -> str:
    return p.replace('\\', '/').replace('*', 'all').replace(':', '__').replace('?', 'in').replace('<', '__').replace(
        '>', '__')
