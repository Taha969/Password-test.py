Password Strength Checker

Overview

This is a simple Python script that uses the re (Regular Expressions) library to validate a user-entered password and determine if it is strong or weak based on a specific criteria. The program will continue to prompt the user for input until a strong password is provided.

Requirements

    Python 3 or newer.

Password Strength Criteria

The script defines a "strong" password as one that strictly adheres to the following regular expression pattern:
^[a-z]+[A-Z]+[!@#$^%]+[0-9]+$

Based on this pattern, a strong password must follow this precise and mandatory sequence of four consecutive groups:

    Starts with: Lowercase letters (a-z).

    Immediately followed by: Uppercase letters (A-Z).

    Immediately followed by: Special symbols (!@#$^%).

    Ends with: Digits (0-9).

Important Note: This pattern requires that each group of characters, symbols, and digits appears at least once and in the exact order specified, with no overlap or other characters in between the groups.

Examples

Password	Strong / Weak	Reason
helloWORLD!@#123	Strong	Matches the pattern: lowercase + uppercase + symbols + digits.
Hello123!	Weak	Incorrect order (starts with uppercase) and does not strictly follow the four groups.
hW!1	Strong	Matches the pattern: h (lower) + W (upper) + ! (symbol) + 1 (digit).

How to Run

    Save the code below into a file named (for example) password_checker.py.

    Open your Terminal or Command Prompt and navigate to the folder where you saved the file.

    Run the script using the following command:

Bash

python password_checker.py

    The program will ask you to enter a password:

    Enter your password: 

    Enter a password and press Enter. The program will loop until you provide a password that matches the strong password criteria.

Code

Python

import re

def is_strong_password(pwd):
    # The pattern enforces a strict order: [lowercase] + [uppercase] + [symbols] + [digits]
    pattern = '^[a-z]+[A-Z]+[!@#$^%]+[0-9]+$'
    return bool(re.search(pattern, pwd))

while True:
    password = input("Enter your password: ")

    if is_strong_password(password):
        print("Strong password")
        break
    else:
        print("\n Password is weak, enter another one ")
