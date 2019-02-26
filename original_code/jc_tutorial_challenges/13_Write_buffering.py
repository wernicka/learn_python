# WRITE BUFFERING - MEDIUM, FUNDAMENTAL, CRITICAL
# IMPORTANT: Import a CSV or text file and do something to each line.  Write the
# new content to a second file, but only write ONCE. (Lesson: file writes are
# expensive/slow!)

f_names = ['5','Fashima', 'Felix', 'Fabio', 'Farah', 'Fay']
new_data = ''

import csv
with open('names.csv', newline='\n') as file:
    data = csv.reader(file, delimiter=',')
    master_list = []
    for row in data:
        master_list.append(row)
    for i in range(6):
        master_list[i].append(f_names[i])

with open('names_with_f.csv', 'w', newline='') as file:
   writer = csv.writer(file)
   for row in master_list:
       writer.writerow(row)