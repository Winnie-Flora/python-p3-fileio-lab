# lib/file_io.py

import os

def write_file(file_name, file_content):
    file_path = f"{file_name}.txt"
    
    with open(file_path, 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    file_path = f"{file_name}.txt"
    
    with open(file_path, 'a') as file:
        file.write(append_content)

def read_file(file_name):
    file_path = f"{file_name}.txt"
    
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.read()
    else:
        return None

# Writing to the file
write_file(file_name="logfile", file_content="Log 1: 5 bananas added\n")

# Appending to the file
append_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted\n")

# Reading the file content
content = read_file(file_name="logfile")
print(content)
