# OOPS (objects -> instances)

# class Info: # generally hum class ke naam ko Capital se likhenge
#     name = "Asif"
#     Roll_No = 40
#     Branch = "Information Technology" # these are some basic properties that a man keep
#     def __init__(self): #contructor alway evoke automatically when object is formed
#         print("Adding some new man info .......") 
      

# man1 = Info()



# class Student:
#     def __init__(self, name, marks, roll):
#         self.name = name
#         self.marks = marks
#         self.roll = roll
#         # print(self)
#         # print("Adding new student....")
#     # define method i.e. a function that belongs to the object
#     def welcome(self):
#         print("Welcome MR. ", self.name)


# s1 = Student("Asif", 99, 40) # hame init function ko call krne ki jrurt nhi pdti hai

# s1.welcome()


# print(s1.name, s1.marks, s1.roll)
# s1 = Student("Arif", 99, 30)
# print(s1.name, s1.marks, s1.roll)
# print(s1)
# print(self.)



# @staticmethod as a decorator

class s:
    @staticmethod
    def sa():
        print("Asif")

s.sa()