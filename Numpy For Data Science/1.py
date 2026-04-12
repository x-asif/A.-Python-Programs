import numpy as np
a = np.array([[1,2,3],
             [1,5,4]])
print(a)
num = int(input("Enter a no: "))
if(num > 0):
    print("Number is positive")
elif(num == 0):
    print("Number is zero")
else:
    print("Number is negative")
    