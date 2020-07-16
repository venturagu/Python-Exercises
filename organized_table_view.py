#! /usr/bin/python3

'''
    This program receives a list of strings and shows it in an organized table
'''


def printTable(tableData):
    colwidths = [0] * len(tableData)

    for i in range(len(colwidths)):
        colwidths[i] = len(max(tableData[i], key=len))

    for li in range(len(tableData[0])):
        for i in range(len(tableData)):
            print(tableData[i][li].rjust(colwidths[i]), end=" ")
        print()


if __name__ == "__main__":
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]
    printTable(tableData)
