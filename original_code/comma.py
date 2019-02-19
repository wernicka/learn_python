# practice problem at the end of Automate the Boring Stuff chapter 4

spam = ['apples', 'bananas', 'tofu', 'cats']

names = ['Hazel', 'Ada', 'Lacey', 'Vera', 'Faith']

def comma_sentence(some_list):
    for i in range(len(some_list) - 1):
        print(f"{some_list[i]},",end=" ")
    print(f"and {some_list[-1]}")

comma_sentence(spam)

def comma_sentence_return(some_list):
    sentence = ""
    for i in range(len(some_list) - 1):
        sentence += f"{some_list[i]}, "
    return f"{sentence}and {some_list[-1]}"

x = comma_sentence_return(names)

print(x)
