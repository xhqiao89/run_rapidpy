import os

def list_files(path):
    for root, directories, filenames in os.walk(path):
        # for directory in directories:
        #     print os.path.join(root, directory)
        for filename in filenames:
            print os.path.join(root,filename)

path = './test_data'
list_files(path)