#! /usr/bin/python3

'''
Manipulating csv file through the csv module
'''

import csv

with open("people.csv") as file:
    print('CSV manipulation 04'.center(30, "*") + '\n')

    for people in csv.reader(file):
        print(("Name:".ljust(15, '.') + " {}" + "\nAge:".ljust(16, '.') +
               "{}").format(*people))

if file.closed:
    print("\nThe csv_manipulating04.py file is closed")
