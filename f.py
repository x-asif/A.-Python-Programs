

# div = a/b
# div = a%b
# div = b%
# div = a//b
# n = int(input("Enter the number: "))
# sum = 0

# while(a>0):
#     b = a % 10
#     sum = sum + b
#     a = a//10



# print("Sum of the digits is : ", sum)


# factorial of a number



# n = int(input("Enter the number: "))
# fact = 1
# while n>0:
#     fact = fact *n
#     n = n-1
# print(fact)


# for fibonacci series

# n = int(input("Enter the number: "))

# a = 0
# b = 1
# print(a , b , end = " ")

# while( n-2):
#     c = a + b
#     a = b
#     b = c
#     print(c, end = " ")
#     n = n - 1


# import numpy as np
# h = np.linspace(1, 10,11)
# # a = np.((2, 3))
# print(h)

# a = int(input("enter a number:"))
# b = int(input("enter b number:"))

# greater = max(a, b)
# while(True):
#     if greater%a == 0 and greater % b ==0:
#         print(greater)
#         break
#     else:
#         greater = greater + 1

    

# year = int(input("enter a year:"))

# if (year%400 ==0) or ((year % 4 == 0 ) and (year%100!= 0)):
#     print("It is a leap year")
# else:
#     print("It is not a leap year")


# def count(s):
#     for str in string.split():
#         s = "&".join(str)
#     return s
# print(count("Python is fun to learn."))

# f = open("asifshaikh.txt","r")
# wrt = f.write("My name is mohammad asif and your name is")
# f.close
# f = open("asifshaikh.txt")
# for line in f:
#     print(line.strip())

# f.close()
# lists = [ "Asisf\n", "Arif\n", "Raja\n"]
# with open("asifshaikh.txt", "a+") as file:
#     k = file.writelines(lists)


# str = input("enter a string :")
 
# count_alpha= 0
# count_digit = 0

# for char in str:
#     if char.isalpha():
#         count_alpha += 1
#     elif char.isdigit():
#         count_digit += 1


# f = open("asifshaikh.txt","w")

# f.write(f"No of letters : {count_alpha}\n")
# f.write(f"No of digits : {count_digit}\n")
# f.close()

import os

if os.path.exists("asifshaikh.txt"):
    os.remove("asifshaikh.txt")
    print(f"The file {"asifshaikh.txt"} is removed successfully")
else:
    print("file doesn't exist")