#! /usr/bin/python3

import sys


def collatz(number):
    if(number % 2 == 0):
        print(str(number // 2))
        return number // 2
    elif (number % 2 == 1):
        print(str(3 * number + 1))
        return 3 * number + 1


def readNumber():
    try:
        number = int(input())

        return number
    except Exception:
        print('Error: An integer value must be entered.')
        sys.exit()


number = readNumber()
while number != 1:
    number = collatz(number)
