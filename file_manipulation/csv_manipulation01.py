#! /usr/bin/python3

file = open("people.csv")
datas = file.read()
file.close()

print('CSV manipulation 01'.center(30,"*") + '\n')
for record in datas.splitlines():
    print(("Name:".ljust(15, '.') + " {}" + "\nAge:".ljust(16, '.') + "{}"+"\n").format(*record.split(',')))
