# Joe Costlow Tutorial Challenges

# QUERY GENERATOR - EASY
# Write a function called query_generator().  The function expects to be passed
# a list of field names.  It then inserts them into the following query, and
# returns the string value of the complete query.
# query = "Select [fieldnames] from database where year = '2019'"
# E.g. fields = ["name", "id", "job"]
#   query_generator(fields) returns:
#   "Select name, id, job from database where year = '2019'"
# Hint: join.


def query_generator(some_list):
    some_list_string = ''
    for item in range(len(some_list) - 1):
        some_list_string += f"{some_list[item]}, "
    some_list_string += some_list[-1]
    return f"Select {some_list_string} from database where year = '2019'"

fields_1 = ["name", "id", "job"]
fields_2 = ["first", "mi", "last", "dob"]

print(query_generator(fields_1))
print(query_generator(fields_2))
