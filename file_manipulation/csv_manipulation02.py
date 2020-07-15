#! /usr/bin/python3

'''
Manipulating csv file using the Stream processing ,
because it has more performance.
It is not necessary to insert a complete file in our program to use your data,
only the necessary parts, so this program accesses the data as needed.

Stream processing refers to a computer programming architecture
in which data is computed directly as it is produced or received.
'''

try:
    file = open("people.csv")

    print('CSV manipulation 02'.center(30, "*") + '\n')

    for record in file:
        print(("Name:".ljust(15, '.') + " {}" + "\nAge:".ljust(16, '.') +
            "{}").format(*record.strip().split(',')))
finally:
    file.close()

if file.closed:
    print("\nThe file is closed")