import re

def is_strong_password(pwd):
    pattern = '^[a-z]+[A-Z]+[!@#$^%]+[0-9]+$'
    return bool(re.search(pattern, pwd))

while True:
    password = input("Enter your password: ")

    if is_strong_password(password):
        print("Strong password")
        break
    else:

        print("\n Password is weak, enter another one ")
