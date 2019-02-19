# Import a CSV that contains columns 0-4.  Print out the columns in a new order:
# 4, 3, 1, 0  (We don't care about column 2 anymore.)

import csv
with open('names.csv', newline='\n') as file:
    data = csv.reader(file, delimiter=',')
    for row in data:
        row = row[4], row[3], row[1], row[0]
        print(' | '.join(row))
