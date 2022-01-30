# keylogger
A simple keylogger developed as an assignment for Information Security Course (CSL 466).

## About
A keylogger that records the keystrokes entered by a user and logs them in a file. Logs files are emailed to a specific address after a specific interval of time. Log files contain system information at the start followed by a list of keys along with the timestamps at which they were pressed and released.

## Installation
- Clone this repo and name it accordingly: ``git clone git@github.com:killtheverse/keylogger.git MY-PROJECT && cd MY-PROJECT``
- Install dependencies: ``pip install -r requirements.txt``

## Usage
- Setup a burner email account. Make sure that 2 factor authentication is disabled. If using a gmail account, make sure that ["Less secure login is enabled"](https://myaccount.google.com/lesssecureapps).
- Create a .env file in the root directory and enter the email credentials as:
```
EMAIL=<YOUR EMAIL>
PASSWORD=<YOUR PASSWORD>
```
For example if your email is `test@example.com` and password is `password123`, then the .env file should look like:
```
EMAIL=test@example.com
PASSWORD=password123
```
- In keylogger.py, change the value of `REPORTING_INTERVAL` and `STOP` to the desired values. `REPORTING_INTERVAL` denotes the interval time (in seconds) after which the emails will be sent with logs. `STOP` if set to `True` will stop the keylogger when the user presses the escape key.
- Run `python keylogger.py`

## Antivirus Test Report
The reports have been generated using [VirusTotal](https://www.virustotal.com/)
- The python script is not detected by any anti virus software - [report](https://www.virustotal.com/gui/file/ff5819b2d7a543e769923ba127411594b7a362ed14ba36620ecf3e253ce75729?nocache=1)

![image](https://user-images.githubusercontent.com/44720416/151691008-5a208b06-b2d8-4c10-865d-60be677ee0a6.png)

- The executable is detected by 20/69 security vendors - [report](https://www.virustotal.com/gui/file/7e4928edf8c8278698922d7b806318a581f4472b391a386b833fd8b754bf962c/detection)

![image](https://user-images.githubusercontent.com/44720416/151691103-3f8c961a-e79f-4f22-bb88-18564aa9918f.png)

![image](https://user-images.githubusercontent.com/44720416/151691110-8993f704-7707-4026-b36b-ed432ef0f0e3.png)

## Todo
- Add additional listeners to keylogger such as capturing screenshots or recording audio.
- Add additional methods to transfer files from host machines.
- Add a functionality so that keylogger automatically starts itself after the boot process.

## Acknowledgments
This project has been inspired by https://github.com/aydinnyunus/Keylogger
