import os
import shutil

# Providing the folder path
origin = r'D:/repo/saurabh1/'
target = r'D:/repo/saurabh2/'

# Fetching the list of all the files
files = os.listdir(origin)

# Fetching all the files to directory
for file_name in files:
    shutil.copy(origin + file_name, target + file_name)
    print("Files are copied successfully")
