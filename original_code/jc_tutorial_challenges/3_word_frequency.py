# WORD FREQUENCY - EASY++
# Given a large block of words, create a dictionary where there is a key for
# each word, and the value is the number of times that the word is encountered.
# Assume that anything separated by space is a word.

import pprint

def word_dictionary_creator(string_in):
    word_dict = {}
    list = string_in.split()
    for i in list:
        word_dict.setdefault(i,0)
        word_dict[i] += 1
    return word_dict

Gettysburg = "Fourscore and seven years ago our fathers brought forth, on this\
 continent, a new nation, conceived in liberty, and dedicated to the\
 proposition that all men are created equal."

pprint.pprint(word_dictionary_creator(Gettysburg))
