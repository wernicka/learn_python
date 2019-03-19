# FILE AGGREGATION 001 - MEDIUM
# Get a list of all CSV files in a directory.  Import them all, combine them,
# and write them out to one aggregated file.

from os import listdir
from os.path import isfile, join
import csv

master_list = []

mypath = "/Users/awernicke/Documents/GitHub/learn_python/original_code/jc_tutorial_challenges/csv_files"

files_and_directories = listdir(mypath)
for file_and_directory_name in files_and_directories:
    path_to_file_or_dir = join(mypath, file_and_directory_name)
    if isfile(path_to_file_or_dir) and path_to_file_or_dir.endswith('.csv'):
        with open(path_to_file_or_dir, newline='\n') as file:
            data = csv.reader(file, delimiter=',')
            for row in data:
                master_list.append(row)

with open('master_file.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for row in master_list:
        writer.writerow(row)