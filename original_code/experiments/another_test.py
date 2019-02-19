def NumberTest(i):
    try:
        val = float(i)
        return True
    except ValueError:
        return False

not_number = "Error message: not a number"
too_small = "Error message: number too small"
too_large = "Error message: number too large"

clean_one_way = ""

def validate(x):
    q = x[0]
    m = x[1]
    c = x[2]
    f = x[3]
    while True:
        print(q)
        k = input()
        if NumberTest(k) is True:
            if float(k) > 0:
                if float(k) <= m:
                    break
                else:
                    print(too_large)
            else:
                print(too_small)
        else:
            print(not_number)
    c = float(k)
    print(f)
    print (" ")

fare = ["""Go to wmata.com and calculate your one way fare.
    Make sure it's the rush hour fare if you commute during rush hour.
    Enter that value here: """, 100, clean_one_way, "fare_feedback"]

validate(fare)
