# FILES/FOLDERS 002 - MEDIUM
# Get a list of all [txt|csv|whatever files in a directory].  Open each one and
# print it to the screen (or print the numbers of lines in the file, or the
# first line - whatever.  Touch each file one way or another.)

from os import listdir
from os.path import isfile, join

mypath = "/Users/awernicke/Documents/GitHub/learn_python/original_code/jc_tutorial_challenges/text_files"

paths_to_files = []
files_and_directories = listdir(mypath)
for file_and_directory_name in files_and_directories:
    path_to_file_or_dir = join(mypath, file_and_directory_name)
    if isfile(path_to_file_or_dir):
        paths_to_files.append(path_to_file_or_dir)

for file in paths_to_files:
    with open(file) as file:
        content = file.read()
        print(content)