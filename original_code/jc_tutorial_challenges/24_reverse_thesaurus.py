# REVERSE DICTIONARY THESAURUS TRANSLATION MAGIC - MEDIUM++
# Import a list of translations where multiple X values can be translated to the
# same Y value.  Generate a report that shows each Y value, how many X values
# can be translated into that Y value, and then a list of those values.

import csv
from collections import defaultdict

mydict = defaultdict(list)
#if you use defaultdict you don't have to use setdefault

with open('./csv_files/thesaurus.csv', newline='\n') as csvfile:
    data = csv.reader(csvfile, delimiter=',')
    for row in data:
        #row type is list
        #adds Y as a dictionary key if it's not already a key, with an empty list as the value
        mydict[row[1]].append(row[0])
        #append X to the value list for that Y's key

for key,value in mydict.items():
    print(f"{key}: {len(value)}: {value}")