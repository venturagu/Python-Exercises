#! /usr/bin/python3

import os

myFiles = ['accounts.txt', 'details.csv', 'invite.docsx']

# file path
for filename in myFiles:
    print(os.path.join(os.getcwd(), filename))

print()

# absolute path
print(os.path.abspath('.'))

# relative path
print(os.path.relpath('.') + '\n')

path =  os.path.join(os.path.abspath('.'), myFiles[0])

# basename
print(os.path.basename(path))

# directory name
print(os.path.dirname(path))

# storing basename and diretory name in a tuple structure
print(os.path.split(path))

# split for all operating systems
print(path.split(os.path.sep))

# get size of this python script
print(os.path.getsize(os.path.join(os.path.abspath('.'), 'path.py')))
print()

# list of strings with file names for each file in this path
print(os.listdir(os.path.relpath('.')))
print()

# total size of files in this current directory
totalSize = 0
for filename in os.listdir():
    totalSize = totalSize + os.path.getsize(os.path.join(os.getcwd(), filename))

print(totalSize)