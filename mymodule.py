
a = int(input("Enter the value of a :"))
b = int(input("Enter the value of b :"))


info = input("Enter the user name:")

c = 10

def greet(name):
    print("Hello",name)

    if a <= b:
        print("A is less than b")
        return
    else:
        print("B is greater than a")

greet(info)