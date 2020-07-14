#! /usr/bin/python3
# pw.py - An insecure program for the password repository

""" To test, run the program with a valid account as an example:
    python3 password_repository.py [account]
    and use the paste command to get the corresponding password.
    Example: Ctrl + v
"""

# associating an account name with a password using a dictionary
import pyperclip
import sys
PASSWORDS = {'email': 'F7minlBDDu',
             'blog': 'Vflkmnhs15',
             'luggage': '1234568'
             }

if len(sys.argv) < 2:
    print(
        "Usage: python password_repository.py [account] - copy account password")
    sys.exit()

account = sys.argv[1]  # the first command line argument is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Password for " + account + " copied to clipboard. ")
else:
    print("There is no account named " + account)
