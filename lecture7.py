# FILE I/O Handling

# open_file = open("lecture7.txt", "r")

# store = open_file.readline()# read one line at a time
# print(store)
# store2 = open_file.readline()# read one line at a time
# print(store2)
# store3 = open_file.readline()# read one line at a time
# print(store3)
# open_file.close()


# f = open("lecture7_new.txt", "r+") #cursor start position pr hota hai aur data ko overwrite kr deta hai start se
# f.write("Ur good")
# store = f.read()
# print(store)
# f.close()



# with syntax



   
# with open("lecture7.txt", "r") as f:
#     data = f.read()
#     print(data) #file close() krne ki jrurat nhi hai with syntax automatically kr deta hai close()


# with open("lecture7.txt", "w") as f:
#     f.write("Python is most easy to understand\n""Guido van rossum is the developer of the python at CWI(informatica)")
    
# with open("lecture7.txt", "r") as f:
#     data = f.read()
#     print(data) #file close() krne ki jrurat nhi hai with syntax automatically kr deta hai close()



# import os
# os.remove("lect.txt")

# with open("Practice_lec7.txt" , "w") as f:
#     f.write("Hi everyone\nWe are learning file I/O\nusing Python\nI like programming in Python")


# with open("Practice_lec7.txt" , "r") as f:
#     data = f.read()
#     print(data)

# new_data = data.replace("Python", "C-language")
# print(new_data)

# with open("Practice_lec7.txt", "w") as f:
#     f.write(new_data)


# count = 0
# with open("split.txt", "r") as f:
#     data = f.read()
#     nums = data.split(",")
#     print(nums)
#     for val in nums:
#         if (int(val)%2 != 0):
            
#             count +=1

# print(count)
        
# with open("split.txt", "r") as f:
#     data = f.read()
#     nums = data.split()
#     print(nums)

file = open("lecture7.txt", "r") #file open krne ke liye open("file_name", "mode")
# save_in1 = file.readline()
# save_in2 = file.readline()

# print(save_in1,save_in2 , "\n abcdefghijklmnopqrstuvwxyz")
# file.close()






            
        
        
    

