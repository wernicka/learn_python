# MIXED-UP FIELD SORTING - MEDIUM
# Import a CSV file that contains fields A,B, C, and D, but the order of the
# fields is never certain.  No matter the input order, convert it so the export
# order is B, A, D, C.  The file will always have reliable headers.

import csv

test_file_in = "/Users/awernicke/Documents/GitHub/learn_python/original_code/jc_tutorial_challenges/csv_files/abcd.csv"

test_file_out = "/Users/awernicke/Documents/GitHub/learn_python/original_code/jc_tutorial_challenges/csv_files/badc.csv"

master_list = []

with open(test_file_in, newline='\n') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    for row in data:
        if "A" in row:
            A = (row.index("A"))
        if "B" in row:
            B = (row.index("B"))
        if "C" in row:
            C = (row.index("C"))
        if "D" in row:
            D = (row.index("D"))
#above lines can be eliminated by using csv dictreader, which will read in the column headers as keys.
        row = row[B], row[A], row[D], row[C]
        master_list.append(row)

with open(test_file_out, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in master_list:
        writer.writerow(row)

