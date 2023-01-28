"""1) calculate file size- padmini (kb, mb)
2) create folder structure using python - Rishi
3) system ip address - neha
4) copy file from one folder type another folder and maintain record of all the copied files
5) current cpu and ram usage - avinash
6) create a txt file that has "hello world" written in it

 put docstrings, use pep8, code must look like it is written by same person
"""

import os

def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0

def file_size(file_path):
    """
    this function will return the file size from [os.stat(file_path).st_size] method
    """
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)
def file_size1(file_path):
    """this function will return file size accordiing to [os.path.getsize(file_path)] method"""
    if os.path.isfile(file_path):
        file_size = os.path.getsize(file_path)
        print(file_size)
        return convert_bytes(file_size)

# Lets check the file size of MS Paint exe
# or you can use any file path
file_path = input("Enter file path without inverted commas:")
print(file_path)
print(file_size(file_path))
print(file_size1(file_path))






