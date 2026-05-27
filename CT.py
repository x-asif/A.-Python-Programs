# f = open("split.txt", "r")
# d = open("lecture7.txt", "r")
# data = f.read()
# data2 = d.read()
# # print(data)
# # print(data2)
# fi= open("split.txt", "w")
# dd = open("lecture7.txt", "w")

# fi = fi.write(data2)

# dd = dd.write(data)


# new = open("split.txt", "r")
# new2 = open("lecture7.txt")
# print(new.read())
# print(new2.read())




# write a program to print even length words in sentence i.e. even lenght words

s = " I am Mohammad Asif. Branch IT. Section A. College REC_ABN" #4


# def word_len(s):
#     w = s.split()
#     for words in w:
#         if len(words)%2 == 0:
#             print(words)
            

            
# sum = lambda a, b: a+b
# print(sum(4, 5))
# arr = [ 1, 2, 3, 4, 5]
# squares = list(map(lambda i : i**2,arr))
# print(squares)


# def facto(n):
#     if n == 0:
#         return 1
#     else:
#         return n*facto(n-1)
    
# result = facto(4)
# print(result)


# name = "Asif"
# def change(name):

#     return name[-1:] + name[1:-1] + name[0:1]
# print(change(name))

# for i in range(1, 8):
#     for j in range(1, i):
#         print("*", end = " ")
#     print()

# name = "asif"
# new = name[-1:]+name[1:-1]+name[:1]
# print(new)

# str1 = input("Enter a string 1:")
# str2 = input("Enter a string 2:")

# common = ""
# for ch in str1:
#     if ch in str2 and ch not in common:
#         common = common + ch
# print(common)


# write a pton programto find the sum all items in a dictionary
d = { "A":100, "B":540, "C":239}

sum = 0
# d = {"A":100, "B":540, "C":239}

# sum = 0

# for value in d.values():
#     sum = sum + value

# print(sum)

lst = ["a", "c", "b", "d", "a","c"]
# common = ""

result = []

for word in lst:

    if word not in result:
        result.append(word)
    # if word == common:
    #     continue
    # else:
    #     common = common + word


# common = list(common)
# print(common)

print(result)
