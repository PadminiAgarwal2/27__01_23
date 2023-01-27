"""
Create folder structure in python

"""
import os

folder = "A"
folder1 = "A1"
folder_name = "A2"
root = "."
path=f"{root}/{folder}/{folder1}/{folder_name}"
print(path)

os.makedirs(path)

folder_name1 ="B"
folder_name2 = "A"
folder_name3 ="B"
folder_name4 = "c"
root = "."
path=f"{folder_name1}/{folder_name2}/{folder_name3}/{folder_name4}"
print(path)

os.makedirs(path)
