from os import remove
from time import sleep
from threading import Thread
from shutil import make_archive

from requests import post


class Sender(Thread):

    def __init__(self, zip_name: str, storage_path: str, storage_folder: str, token: str, user_id: int, processes_pause: int, clear_logs):
        Thread.__init__(self, name="sender")

        self.zip_name = zip_name
        self.storage_path = storage_path
        self.storage_folder = storage_folder
        self.processes_pause = processes_pause

        self.token = token
        self.user_id = user_id

        self.clear_logs = clear_logs

    def __create_archive(self):

        make_archive(f"{self.storage_path}{self.zip_name}", 'zip', f"{self.storage_path}{self.storage_folder}")

    def __send_archive(self):

        with open(f"{self.storage_path}{self.zip_name}.zip", 'rb') as file:

            post(
                url=f"https://api.telegram.org/bot{self.token}/sendDocument",
                data={
                    'chat_id': self.user_id
                },
                files={
                    'document': file
                }
            )

        file.close()

    def __delete_files(self):

        self.clear_logs()
        remove(f"{self.storage_path}{self.zip_name}.zip")

    def run(self):

        while True:
            sleep(self.processes_pause)
            self.__create_archive()
            self.__send_archive()
            self.__delete_files()
