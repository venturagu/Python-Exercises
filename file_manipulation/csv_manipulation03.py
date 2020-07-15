#! /usr/bin/python3

'''
Manipulating csv file using Stream processing,
and closing the file using the reading block with 'WITH "

Writing output to another file called 'people.txt'
'''

with open("people.csv") as file:
    with open("people.txt", "w") as saida:
        print('CSV manipulation 03'.center(30, "*") + '\n', file=saida)

        for record in file:
            people = record.strip().split(',')
            print(("Name:".ljust(15, '.') + " {}" + "\nAge:".ljust(16, '.') +
                   "{}").format(*people), file=saida)

if file.closed:
    print("\nThe csv_manipulating03.py file is closed")

if saida.closed:
    print("\nThe saida.txt file is closed")
