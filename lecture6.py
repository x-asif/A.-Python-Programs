# FUNCTIONS AND RECURSION
# Block of statements to perform some specific task

# def sum(a, b): # Function definition 
#     s = a + b 
#     # return s
#     print(s)
# print("sum of the givern numbers is " , sum(2, 3)) # function call


names = [ "Asif", "Arif", "Raja", "Ayasha", "Alishba"]
# def calc_len(lists):
#     return len(lists)


# k = calc_len(names)
# print(k)

# nums = [ 1, 3, 4, 2,4, 5, 3, 2, 4, 5, 3, 3]
# abc = [ "a" , "b", "c" , "d"]

# def calc_len(lists):
#     print(len(lists))

# calc_len(names)
# calc_len(nums)
# calc_len(abc)

# WAP to find the factorial of n
# n = int(input("Enter the number:"))
# j = 1
# def facto(k):
#     for i in range(k, 0, -1):
#         j = j * i
#         return j
# facto(n)
# print(j)


# Recursion

# def facto(n):
#     if(n == 0 or n ==1):
#         return 1
#     else:
#         return n*facto(n-1)
    
# l = (facto(5))
# print(l)

k = int(input("Enter the number: "))
def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n -1) + n
sum = calc_sum(k)
print(sum)