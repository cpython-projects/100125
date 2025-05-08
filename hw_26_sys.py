import sys
import os

_, dir_path = sys.argv # ['hw_26.py', '/home/user/documents']

dirs = []
files = []

for obj_name in os.listdir(dir_path):
    if os.path.isdir(obj_name):
        dirs.append(obj_name)
    else:
        files.append(obj_name)

print('Folders:')
print(*dirs, sep='\n')

print('Files:')
print(*files, sep='\n')

