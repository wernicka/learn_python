# FILES/FOLDERS 002 - MEDIUM
# Get a list of all [txt|csv|whatever files in a directory].  Open each one and
# print it to the screen (or print the numbers of lines in the file, or the
# first line - whatever.  Touch each file one way or another.)

from os import listdir
from os.path import isfile, join

mypath = "/Users/awernicke/Documents/GitHub/learn_python/original_code/jc_tutorial_challenges/text_files"

#list comprehension from https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
#onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

#Amey's rewriting of onlyfiles above
onlyfiles = []
files_and_directories = listdir(mypath)
for file_and_directory_name in files_and_directories:
    path_to_file_or_dir = join(mypath, file_and_directory_name)
    print("file_and_directory_name = ", file_and_directory_name)
    print("path_to_file_or_dir = ", path_to_file_or_dir, "\n")
    if isfile(path_to_file_or_dir):
        onlyfiles.append(file_and_directory_name)



for file in text_files/onlyfiles:
    # thing = open(file)
    # content = thing.read()
    # thing.close()
    # print(content)
    with open(file) as file:
        content = file.read()
        print(content)


# with open('names.csv', newline='\n') as file:
#     data = csv.reader(file, delimiter=',')
#     master_list = []
#     for row in data:
#         master_list.append(row)
#     for i in range(6):
#         master_list[i].append(f_names[i])