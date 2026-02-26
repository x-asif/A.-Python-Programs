# LIST AND TUPLES

# roll_no = [ 40, 40, 23, 23, 12, 23, 34, 25]
# print(roll_no)
# print(len(roll_no))
# print(roll_no[:len(roll_no)])#if we miss the starting index then counting of index is start from a[0]
# roll_no[1] = 1
# print(roll_no)
# print(type(roll_no))


#list specific method(function)
# list= [12, 1, 3, 2, 4, 5]
# print(list)
# list.append(11111) # this is why list is mutable changes can occurs in list
# print(list) 
# list.reverse()
# print(list)
# list.sort()
# print(list)
# list.sort(reverse = True)
# print(list)
# list.reverse() #list is reverse
# print(list)
# list.insert(1, 2000)
# print(list)
# print(list.sort())
# print(list)
# list.remove( 12)
# print(list)


# TUPLE ()
"""
A built in data type that let us create IMMUTABLE Sequence of values.

"""

# tup = (1, 4, 2, 5, 2, 4, 3, 6, 6, 6, 4, 1)
# print(type(tup))
# print(tup[4])

# tup = ()
# print(tup)
tup = (12, (4, (1, (2, (9, ("asif", 20, 40, "Information Technology"))))))
print(tup[0:1])
print(len(tup))
