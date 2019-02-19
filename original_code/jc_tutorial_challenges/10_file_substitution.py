# FILE SUBSTITUTION - EASY
# Import a text file that contains generic text (i.e. a passage from a book or
# news article.)  Replace every occurence of word X with word Y.
# Write it to a file

file = open('quotes_about_family.txt')
content = file.read()
file.close()

def word_replacement(text, old_word, new_word):
    split_text = text.split()
    for i in range(len(split_text)):
        if split_text[i] == old_word:
            split_text[i] = new_word
    return ' '.join(split_text)

#sample_sentence = "My family is the best thing to ever happen to me."
#print(word_replacement(sample_sentence, "family", "dog"))
new_content = (word_replacement(content, "family", "cat"))

new_file = open('quotes_about_cat.txt', 'w')
new_file.write(new_content)
new_file.close()

# Doesn't replace if there is punctuation right next to the word because
# I'm splitting on spaces and not on punctuation.
# Doesn't preserve new line characters becuase I'm splitting on spaces and
# new line characters but only putting spaces back in with the join.
# Previous exercise said assume that anything separated by space is a word.
# Use https://stackoverflow.com/questions/19894478/regex-punctuation-split-python/19894589 to split on words instead
