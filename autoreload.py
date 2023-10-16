import os
import time
import subprocess

# Your main Tkinter application script
tkinter_script = "./attendese\maintry.py"

# Function to check if the file has been modified
def is_file_modified(path, last_modified_time):
    return os.path.getmtime(path) > last_modified_time

# Function to run the Tkinter script
def run_tkinter_script():
    subprocess.run(["python", tkinter_script])

if __name__ == "__main__":
    last_modified_time = 0

    while True:
        if is_file_modified(tkinter_script, last_modified_time):
            print("Reloading Tkinter script...")
            last_modified_time = time.time()
            run_tkinter_script()
        time.sleep(1)  # Check every second for changes
