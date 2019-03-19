# REVERSE DICTIONARY THESAURUS TRANSLATION MAGIC - MEDIUM++
# Import a list of translations where multiple X values can be translated to the
# same Y value.  Generate a report that shows each Y value, how many X values
# can be translated into that Y value, and then a list of those values.

import csv

#mydict = {}

with open('./csv_files/thesaurus.csv', newline='\n') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    Y_values = []
    X_values = []
    Y_value_count = 0
    for row in data:
        #row type is list
        if row[1] not in Y_values:
            Y_values.append(row[1])
        for Y_value in Y_values:
            Y_value_count += 1
            X_values.append(row[1],row[0])

print(Y_values)
print(X_values)

        # key = row[Y]
        # val = row[X]
        # mydict[key] = (val)

        # file = open('inventory.csv')
        # content = file.read()
        # file.close()
        #
        # my_things = {}
        # split_content = content.split("\n")
        # # split_content type is list
        # for line in split_content:
        #     # line type is string
        #     line = line.strip()
        #     if line:
        #         (key, val) = line.split(",")
        #         my_things[key] = int(val)
        #
        # for key, val in my_things.items():
        #     print(f"{key} : {val}")