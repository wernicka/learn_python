flag2 = True
while flag2:
    print("Do you take public transit year round, in all seasons?")
    x = input().lower()
    if x in ("yes", "y"):
        flag2 = False
    elif x in ("no", "n"):
        flag2 = False
    else:
        print("Please answer yes or no.")
print(x)
