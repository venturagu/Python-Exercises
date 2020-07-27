#! /usr/bin/python3
# phoneAndEmail.py - Find phone numbers and email address on the clipboard

import re
import pyperclip

# extracts phone number
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?               # area code  -> either 561 or  (561)
    (\s|-|\.)?                       # separator  (if there is)
    (\d{3})                          # first 3 digits
    (\s|-|\.)                        # separator
    (\d{4})                          # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?   # extension
    )''', re.VERBOSE)

# extracts email
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                # username
    @                                # @symbol
    [a-zA-Z0-0._%+-]+                # domain name
    (\.[a-zA-Z]{2,4})                # dot something
    )''', re.VERBOSE)

# find matches in clipboard text.
text = str(pyperclip.paste())  # paste all string in to 'text' string
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != ' ':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard. (our new string)
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers of email addresses found.')
