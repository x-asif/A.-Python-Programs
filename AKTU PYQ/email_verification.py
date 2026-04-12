import re

def validate_email(email):
    pattern = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    if re.match(pattern, email):
        print("Valid Email")
    else:
        print("Invalid Email ID")

# input from the user

email = input("Enter emial:")
validate_email(email)
# print(validate_email(email))