#! /usr/bin/python3
# strip_using_regex.py - It is a version of the python string strip () method using regex

import re

def strip(string, characteres=" "):
    if(characteres == " "):
        string = re.sub('^\s+|\s+$', '', string)
    else:
        for i in range(len(characteres)):
            if(" " in string and " " in characteres[i]):
                string = re.sub('^\s+|\s+$', '', string)
            else:
                string = re.sub(
                    '^['+characteres+']+|['+characteres+']+$', '', string)
    return string

# Simple test suite to validate the implemented method
string = '  xoxo love xoxo   '

print(strip(string))
print(strip(string, ' xoe'))
print(strip(string, 'stx'))

string = 'android is awesome'
print(strip(string, 'an'))
