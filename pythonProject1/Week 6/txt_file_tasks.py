import os


def cwd():
    path = os.getcwd()
    print(f"The current working directory is {path}")
    print("The directory contains the following file:")
    for each_file in os.listdir(path):
        print(each_file)

def run():
    print("Processing...")
    cwd()



run()
