#! /usr/bin/python3

'''
Extract the fourth and ninth fields from the IBGE csv file
 or the ninth and eighth fields according to the URL passed to download a csv file
'''

import csv
from urllib import request


def readLocalFile(file):
    with open(file, encoding='ISO 8859-1') as file:
        for record in csv.reader(file):
            print(f'{record[3]} : {record[9]}')


def readExternalFile(url):
    with request.urlopen(url) as inputFile:
        print('Downloading the csv'.ljust(20, '.'))
        datas = inputFile.read().decode('latin1')
        print('Complete download!')

        i = 0
        for city in csv.reader(datas.splitlines()):
            print(f'{city[9]} : {city[8]}')
            if (i >= 70):
                break
            i += 1


if __name__ == "__main__":
    import sys
    readLocalFile(sys.argv[1])

    print()
    input("Enter any tecle to continue ... \n")
    
    readExternalFile(
        r'https://people.sc.fsu.edu/~jburkardt/data/csv/cities.csv')
