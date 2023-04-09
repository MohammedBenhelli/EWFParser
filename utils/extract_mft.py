from utils.constants import load_constants

# TODO: parse_MFT
def extract_mft(data_partition_fs, dest: str):
    print(f"Extracting MFT")
    CONFIG = load_constants()
    fileobject = data_partition_fs.open(CONFIG['MFT_PATH'])
    with open(f"{dest}/{fileobject.info.name.name.decode()}", 'wb') as f:
        f.write(fileobject.read_random(0, fileobject.info.meta.size))
