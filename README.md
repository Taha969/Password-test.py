Password Strength Checker 🔒

A simple Python utility that validates password strength based on a specific character sequence using Regular Expressions (Regex).
📝 Description

This script prompts the user to enter a password and checks it against a predefined security pattern. Unlike general checkers, this script enforces a strict order of character types.
Password Criteria:

To be considered "Strong" by this script, the password must follow this exact sequence:

    Lowercase letters (a-z) at the beginning.

    Uppercase letters (A-Z) following the lowercase.

    Special characters (!@#$^%) following the uppercase.

    Digits (0-9) at the end.

🔍 Regex Breakdown

The script uses the following pattern:

^[a-z]+[A-Z]+[!@#$^%]+[0-9]+$
Symbol	Description
^	Asserts the start of the string.
[a-z]+	One or more lowercase English letters.
[A-Z]+	One or more uppercase English letters.
[!@#$^%]+	One or more special characters from the set.
[0-9]+	One or more digits (0-9).
$	Asserts the end of the string.
🚀 How to Use

    Prerequisites: Ensure you have Python 3.x installed.

    Run the script:
    Bash

    python your_script_name.py

    Input: Enter a password when prompted. The script will keep asking until a "Strong" password is provided.

Examples:
Password	Status	Reason
lowUP#12	✅ Strong	Matches the exact order (lower, upper, symbol, digit).
12lowUP#	❌ Weak	Wrong order (starts with numbers).
lowUP12	❌ Weak	Missing special characters.
LOWlow#12	❌ Weak	Wrong order (starts with uppercase).
