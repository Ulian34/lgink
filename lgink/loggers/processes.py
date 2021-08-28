from time import sleep
from os import remove, path
from datetime import datetime
from threading import Thread

from psutil import process_iter


class ProcessesLogger(Thread):

    def __init__(self, storage_path: str, storage_folder: str, processes_pause: int):
        Thread.__init__(self, name="processes")

        self.processes = []
        self.processes_pause = processes_pause

        self.storage_path = storage_path
        self.storage_folder = storage_folder

    def __check_processes(self):

        for process in process_iter():

            self.process = f"[{datetime.fromtimestamp(process.create_time())}] [{process.status()}] [{process.cpu_percent()}] [{process.memory_percent():.4f}] {process.name()}"

            if self.process not in self.processes:

                self.processes.append(process.name())
                self.__log_processes()

            else:

                continue

    def __log_processes(self):

        with open(f'{self.storage_path}{self.storage_folder}processes_logger.txt', 'a', encoding='utf-8') as self.processes_logger:
            self.processes_logger.write(self.process + "\n")

    def clear(self):

        if path.exists(f'{self.storage_path}{self.storage_folder}processes_logger.txt'):

            try:

                self.processes_logger.close()

            except:

                pass

            remove(f'{self.storage_path}{self.storage_folder}processes_logger.txt')
            self.processes.clear()

    def run(self):

        while True:
            self.__check_processes()
            sleep(self.processes_pause)
