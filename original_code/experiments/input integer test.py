def NumberTest(i):
    try:
        val = float(i)
        print(True)
    except ValueError:
        print(False)

NumberTest(2.55)

#weeks_vacation = input("""About how many weeks this year were you on vacation or leave? """)
#need an if or while statement to check the validity of each input

#while (weeks_vacation.isdigit() != True):
    #print(False)
    #weeks_vacation = input("""About how many weeks this year were you on vacation or leave? """)

#print(True)
