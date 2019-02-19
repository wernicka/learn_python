# FILE WORD FREQUENCY - EASY
# Import a text file; count how many times each word in it is encountered

import pprint


def word_dictionary_creator(string_in):
    word_dict = {}
    list = string_in.split()
    for i in list:
        word_dict.setdefault(i,0)
        word_dict[i] += 1
    return word_dict


file = open('../inventory.txt')
content = file.read()
file.close()

pprint.pprint(word_dictionary_creator(content))
