# Joe Costlow Tutorial Challenges

# Write a function called chop().  Chop receives two parameters: data, and length
# It returns data after truncating it to length.
# E.g. chop("Joseph", 3) returns 'Jos'
# E.g. chop("Sean", 4) returns 'Sean'
# E.g. chop("cmoses@eab.com", 10) returns 'cmoses@eab'
# E.g. chop(123456789, 5) returns '12345'
# Note: The data parameter might be a string or a numeric; be able to handle
# either.
# Hint: slice.

def chop(data,length):
    data = str(data)
    length = int(length)
    return data[0:length]

print(chop("Joseph", 3))
print(chop("Sean", 4))
print(chop("cmoses@eab.com", 10))
print(chop(123456789, 5))
