# WAP A PROGRAM TO PRINT NUMBERS FROM 1 TO 100

# i = 1
# while i <= 100:
#     print(i)
#     i +=1


# WAP TO PRINT NUMBERS FROM 100 TO 1

# i = 100
# while i >= 1:
#     print(i)
#     i -= 1

# # n = int(input("Enter the number: "))
# # i = 1
# # while i <= 10:
# #     print(n*i)
# #     i += 1

# # WAP TO PRINT THE LIST ELEMENTS USING LOOP 

# i = 0
# x = 3 # lets x is 3
# lists = [1, 3, 2, 5, 6, 4, 7, 4, 3]
# print(type(lists))
# print(lists[0])
# l = len(lists)
# print(l)
# while i < 9:
#     print(lists[i])
#     i += 1




# i =0
# x = 10 # lets x is 3
# lists = (1, 3, 2, 5, 6, 4, 7, 4, 3)
# print(type(lists))
# print(lists[0])
# l = len(lists)
# count = 0
# print(l)
# while i < 9:
#     if(x == lists[i]):
#         print("Element is present in the list")
#         count = 1
#         break
#     i +=1
# if(count == 0):
#     print("Element not found in list")





# i = 1 
# while i <= 5:
#     if ( i == 4):
#         print("Now i am skipping the word 4 from the sequence")
#         i += 1
#         continue
#     print(i)

#     i += 1






i = 1
while i <= 10:
    if(i%2 == 0):
        i += 1
        continue
    print(i)
    i += 1