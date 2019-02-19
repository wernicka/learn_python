spam = {'color': 'red', 'age': 42}
for v in spam.values():
  print(v)

for k in spam.keys():
    print(k)

for i in spam.items():
    print(i)

x = list(spam.keys())
print(x)

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
                'Bob': {'ham sandwiches': 3, 'apples': 2},
                'Carol': {'cups': 3, 'apple pies': 1}}

for k in allGuests.keys():
    print(k)

for v in allGuests.values():
    print(v)

for i in allGuests.items():
    print(i)

print(list(allGuests.keys()))

#print(list('Alice'.values()))

#for k in allGuests.keys():
#    print(list(k.values()))

for k, v in guests.items():
    print(list(v))
