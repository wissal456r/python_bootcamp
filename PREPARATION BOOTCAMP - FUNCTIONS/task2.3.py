import os

def list_directory(path):
    for name in sorted(os.listdir(path)):
        full_path = os.path.join(path, name)
        print(full_path)

        if os.path.isdir(full_path):
            list_directory(full_path)

list_directory(".")
