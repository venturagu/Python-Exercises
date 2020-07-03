""" Prints a list with a better view

    This script allows the user to place some items he needs in
    a list data structure and after that the list is printed as
    a string with commas separating each item and the word
    AND before the last item.
"""

span = []


def readList(span):
    while True:
        try:
            number = int(input('How many items will be in your list? '))
            for i in range(number):
                item = input('Enter your ' + str(i+1) + 'º ' + 'item: ')
                span.append(item)
        except Exception:
            print('Error: An integer value must be entered. \n')
            continue
        break


def listToString(span):
    result = ''

    if(len(span) == 2):
        result = str(span[0]) + ' and ' + str(span[1])
    else:
        for i in range(len(span)-1):
            result += str(span[i]) + ', '
        result += 'and ' + str(span[-1])
    print(result)

readList(span)
listToString(span)
