import os
import sys
import shutil
import time
import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from os import listdir
from os.path import isfile, join

# Log file auto_file_organizer
log = open("auto_file_organizer_log.txt", "w")


class MyHandler(FileSystemEventHandler):

    def on_created(self, event):
        files = [f for f in listdir(folder_to_track) if isfile(join(folder_to_track, f))]
        # Destination Subfolders for group by file type
        dest_sub_folder = ["Pictures/", "Documents/", "Presentation/", "Scripts/", "Compressed/", "Programs/", "Others/"]

        try:
            # Create Subfolders in Destination Directory if not exists
            for sub_folder in dest_sub_folder:
                os.mkdir(folder_destination + sub_folder)
        except:
            pass

        for file in files:
            src = folder_to_track + file
            if not src.endswith(".crdownload"):
                if src.endswith(('.jpg', '.jpeg', '.png', '.svg')):
                    new_destination = folder_destination + dest_sub_folder[0] + file
                elif src.endswith(('.doc', '.docx', '.csv', '.xlsx', '.xml', '.pdf', '.txt')):
                    new_destination = folder_destination + dest_sub_folder[1] + file
                elif src.endswith(('.pptx', '.ppt')):
                    new_destination = folder_destination + dest_sub_folder[2] + file
                elif src.endswith(('.py', '.html', '.ipynb', '.yml', '.json', '.js', '.java')):
                    new_destination = folder_destination + dest_sub_folder[3] + file
                elif src.endswith(('.zip', '.rar', '.iso', '.tar.xz', '.tar.gz')):
                    new_destination = folder_destination + dest_sub_folder[4] + file
                elif src.endswith(('.exe', '.msi', '.deb', '.tar')):
                    new_destination = folder_destination + dest_sub_folder[5] + file
                else:
                    new_destination = folder_destination + dest_sub_folder[6] + file

                time_now = str(datetime.datetime.now())
                try:
                    shutil.move(src, new_destination)
                    # WRITING LOG DATA
                    log_data = "\t" + time_now + " -- FILE MOVED FROM --" + src + " -- TO -- " + new_destination+"\n"
                    log.write(log_data)
                    log.flush()
                except Exception as e:
                    # WRITING LOG DATA
                    log_data = "\t" + time_now + " -- Exception --" + e+"\n"
                    log.write(log_data)
                    log.flush()


folder_to_track = "/home/user/Downloads/"  # Enter The Source Folder
folder_destination = "/home/user/Desktop/Downloaded_files/"  # Enter The Destination Folder
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
