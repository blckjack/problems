import os

list_of_dirs = []


def get_list_of_dirs(directory):
    for item in os.listdir(directory):
        full_path = os.path.join(directory, item)
        if os.path.isdir(full_path):
            get_list_of_dirs(full_path)
            list_of_dirs.append(full_path)

get_list_of_dirs("/tmp/")

print list_of_dirs
