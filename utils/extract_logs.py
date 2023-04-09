import Evtx.Evtx as evtx
import Evtx.Views as e_views

from utils.constants import load_constants
from utils.file import check_dir_exist


def extract_logs(data_partition_fs, dest: str):
    check_dir_exist(dest)
    CONFIG = load_constants()
    logs_dir_object = data_partition_fs.open_dir(CONFIG['LOGS_DIR_PATH'])

    for entry in logs_dir_object:
        if entry.info.name.name.decode() in CONFIG['LOGS_FILES']:
            filepath = CONFIG['LOGS_DIR_PATH'] + "/" + entry.info.name.name.decode()
            print(f"Extracting {filepath} logs")
            fileobject = data_partition_fs.open(filepath)
            with open(f"{dest}/{fileobject.info.name.name.decode()}", 'wb') as f:
                f.write(fileobject.read_random(0, fileobject.info.meta.size))
            with evtx.Evtx(f"{dest}/{fileobject.info.name.name.decode()}") as log, open(f"{dest}/{fileobject.info.name.name.decode()}.xml", "w") as e:
                e.write(e_views.XML_HEADER)
                e.write("<Events>")
                for record in log.records():
                    e.write(record.xml())
                e.write("</Events>")
