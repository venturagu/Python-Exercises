"""
    1. Search for American date patterns in text with slash, dot, or hyphen options
       Month/Day/Year -> month number/ day number / all year
       example: 02/24/2018 or 02.24.2018 or 02-24-2018
    
    2. Validation in a text to verify a date equal to the current date (Month/Day/Year)

    3. Replace one pattern with another. Insert a date in Brazilian format and print in American format

    4. Make sure the password is in the correct format. The password must have:
        at least one capital letter
        at least two special characters
        at least eight digits
        at least three numbers
"""

import re
from datetime import date
from clear import clear
import time

today = date.today()

currentDate = today.strftime('%m/%d/%Y')

text = """07/22/203 Things work better for those who get the best out of how things work. 12.05.2018

123 To live a creative life, we need to lose the fear of being wrong.. 12-30-2020

2020/12.03 Opportunities don't happen, you create them. 03/24/2019

12.05/000 I have not failed. I just found 10,000 ways that don't work. 80/56/1999 """ + currentDate

text2 = "Test with one date 03/24/2019"


#  Search for American date patterns in text with slash, dot, or hyphen options
def searchDatePatterns(text):
    dateRegex = re.compile(
        r'(0[1-9]|1[0-2])[/.-](0[1-9]|[1-2][0-9]|3[0-1])[/.-]\d{2}(\d{2})')
    mo = dateRegex.findall(text)

    if not mo:
        print("\nThis text has no date")
    else:
        msg = "\nDates found:" if len(mo) >= 2 else "\nDate found:"
        print(msg + "\n")

        for li in range(len(mo)):
            for i in range(len(mo[0])):
                if(i == (len(mo[0]) - 1)):
                    print(mo[li][i], end="")
                else:
                    print(mo[li][i], end="/")
            print()


def currentDateValidation(text):
    month = today.strftime('%m')
    year = today.strftime('%Y')
    day = today.strftime('%d')

    dateRegex = re.compile(r'{}[/.-]{}[/.-]{}'.format(month, day, year))
    mo = dateRegex.findall(text)

    if not mo:
        print("\nThis text has no current date")
    else:
        print("\nThe current date was found: " + mo[0])


# Replace one pattern with another. Insert a date in Brazilian format and print in American format
def changeDateFormat():
    dateRegex = re.compile(
        r'(0[1-9]|[1-2][0-9]|3[0-1])[/.-](0[1-9]|1[0-2])[/.-]\d{2}(\d{2})')

    while(1):
        try:
            userDate = input('\nInput a date in brazilian format\
(day/month/year example: 05/20/2020),\n\
you can use slash "/", dot "." or hyphen "-":  ')
            mo = dateRegex.match(userDate)
            day = mo.group(1)
            month = mo.group(2)
            americanFormat = month + "/" + day + "/" + mo.group(3)
            print("\nBrazilian date format: " + mo.group(0))
            print("\nAmerican date format: " + americanFormat)
            break
        except(Exception):
            clear()
            print("\n\033[1;31mError\033[m \
- Please put a date again with correct format")


# Make sure the password is in the correct format.
def passwordValidation():
    senhaRegex = re.compile(
        r'^(?=.*\d{1}.*\d{1}.*\d{1})(?=.*[a-z])(?=.*[A-Z])(?=.*[#?!@$%^&*-]).{8,15}$')

    while(1):
        try:
            print("""\nThe password need have:\n 
    at least one capital letter
    at least two special characters
    at least eight digits and a maximum of 15
    at least three numbers\n""")

            senha = input("Enter a password: ")
            mo = senhaRegex.match(senha)
            print("\n\033[92m" + str(mo[0]) + "\033[m is a valid password!")
            break
        except(Exception):
            clear()
            print("\n\033[1;31mInvalid Password\033[m \
- Please enter a valid password")


searchDatePatterns(text)
searchDatePatterns(text2)
currentDateValidation(text)
currentDateValidation(text2)
changeDateFormat()
passwordValidation()
