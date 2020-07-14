#! /usr/bin/python3

"""The challenge is construct a script to a fantasy game inventory which be have follows features:

1. Insert players into a team
2. Item count (total and specific element)
3. Team average and player average
4. Highest and lowest average score on the team
5. Filter if a player has the same number as another player for a specific item
6. Filter if a player has at least one item

The focus is on practicing how to use the dictionary and list data structure for problem solving
"""

import pprint
import copy
import sys
from os import system, name
import time
from collections import Counter


# define a clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def insertion(player):
    number = int(input("How many players will be your time? "))

    gamers_list = []

    for i in range(number):
        gamers_list.append(copy.copy(player))

    while True:
        try:
            for i in range(number):
                print("\nEnter how many elements the " +
                      str(i+1) + "º player have to each item: ")
                gamers_list[i]['arrow'] = int(input("Arrow: "))
                gamers_list[i]['dagger'] = int(input("Dagger: "))
                gamers_list[i]['gold coin'] = int(input("Gold coin: "))
                gamers_list[i]['rope'] = int(input("Rope: "))
                gamers_list[i]['torch'] = int(input("Torch: "))
        except Exception:
            print('Error: An integer value must be entered. \n')
            time.sleep(1)  # Sleep for 1 second
            clear()
            continue
        break

    print("\n....................Team structure....................\n")
    pprint.pprint(gamers_list)
    return gamers_list


# Item count feature (total and specific element)
def countTeam(team):
    counter = Counter(team[0])
    for i in team[1:]:
        counter += Counter(i)

    print("\n.........................Count.........................\n")
    for k, v in counter.items():
        print(k + " : " + str(v))

    return counter


def countTotalTeam(counter):
    total = 0
    for value in counter.values():
        total = total + value
    return(total)


def countItem(counter, item):
    numberItems = 0

    for i in counter:
        numberItems = counter.get(item, 0)

    if(numberItems == 0):
        print("There is no " + item + " item present in this team")
    else:
        print("There is " + str(numberItems) + " " + item + " in this team")


# Team average and player average features
def teamAverage(counter):
    average = countTotalTeam(counter)
    average = average / 2

    print("Team average: " + str(average))


def playerAverage(team, player):
    gamer = Counter(team[player])
    average = countTotalTeam(gamer) / 2
    return(average)


# Highest and lowest average score on the team
def highest_lowest_average(team):
    maxValue = playerAverage(team, 0)
    minValue = playerAverage(team, 0)
    indice = 0
    for i in team[1:]:
        indice += 1
        if(playerAverage(team, indice) > maxValue):
            maxValue = playerAverage(team, indice)
        elif(playerAverage(team, indice) < minValue):
            minValue = playerAverage(team, indice)

    print("\nHighest average score on the team: " + str(maxValue))
    print("\nLowest average score on the team: " + str(minValue))


# Filter if a player has the same number as another player for a specific item
def checkSameItem(team, item):
    sameItemsList = []
    for i in range(len(team)):
        sameItemsList.append(team[i][item])

    lenList = len(sameItemsList)
    lenSet = len(set(sameItemsList))

    difference = (lenList - lenSet) + 1
    if(lenList != lenSet):
        print("In this team have " + str(difference) +
              " players  with the same number of " + item + " item")
    else:
        print("There are no players with same number of " + item + " item")

    pprint.pprint(sameItemsList)


# Filter if a player has at least one item
def check_player_isEmpty(team, player):
    gamer = Counter(team[player])
    for value in gamer.values():
        if(value != 0):
            return(False)
    return(True)


def chooseItem():
    while True:
        item = input("\nWhich item do you want to check in your team? \
        (arrow, dagger, gold coin, rope, torch) ")
        item = item.lower()
        if(item != 'arrow' and item != 'dagger' and item != 'gold coin' and item != 'rope' and item != 'torch'):
            print(
                "\n\033[1;31mError\033[m - Please, write a valid item correctly")
            continue
        break

    return(item)


def choosePlayer():
    while True:
        try:
            player = int(input("\nWhich player do you want to check? \
    Put your position as number (0 is the first player and " + str(len(team)-1) + " is the last): "))
            if(player < 0 or player > (len(team)-1)):
                continue
            return(player)

        except Exception:
            print(
                "\n\033[1;31mError\033[m - Please enter a number referring to the player's position")
            time.sleep(5)  # Sleep for 3 seconds
            clear()
            continue
        break


def menu(team, player):
    counter = countTeam(team)
    clear()
    while True:
        print("\n************MAIN MENU**************\n")

        choice = int(input("""
    1. Insert players into a team
    2. Item count (total and specific element)
    3. Team average and player average
    4. Highest and lowest average score on the team
    5. Filter if a player has the same number as another player for a specific item
    6. Filter if a player has at least one item
    7. Exit

    Please enter your choice: """))

        if choice == 1:
            clear()
            team = insertion(player)
            counter = countTeam(team)
        elif choice == 2:
            while True:
                clear()
                print("\n************ITEM COUNT**************\n")
                subChoice = int(input("\n1. Total\n2. Specific element\n3. Return\n4. Exit\n "))
                if(subChoice == 1):
                    total = countTotalTeam(counter)
                    print("\nTotal: " + str(total))
                elif(subChoice == 2):
                    item = chooseItem()
                    countItem(counter, item)
                elif(subChoice == 3):
                    break
                elif(subChoice == 4):
                    clear()
                    sys.exit()
                else:
                    continue

                input("\nEnter to continue: ")
        elif choice == 3:
            while True:
                clear()
                print("\n**************AVERAGE****************\n")
                subChoice = int(input("\n1. Team average\n2. Player average\n3. Return\n4. Exit\n "))
                if(subChoice == 1):
                    teamAverage(counter)
                elif(subChoice == 2):
                    player = choosePlayer()
                    average = playerAverage(team, player)
                    print("\nPlayer average: " + str(average))
                elif(subChoice == 3):
                        break
                elif(subChoice == 4):
                    clear()
                    sys.exit()
                else:
                    continue

                input("\nEnter to continue: ")
        elif choice == 4:
            clear()
            print("\n**************HIGHEST AND LOWEST AVERAGE - TEAM****************\n")
            highest_lowest_average(team)
        elif choice == 5:
            clear()
            print("\n**************CHECK SAME AMOUNT****************\n")
            checkSameItem(team, 'arrow')
        elif choice == 6:
            clear()
            print("\n**************CHECK PLAYER WITHOUT ITEM****************\n")
            player = choosePlayer()
            playerEmpty = check_player_isEmpty(team, player)
            if(playerEmpty):
                print("The player in the " + str(player) +
                    " position doesn't have any item")
            else:
                print("The player in the " + str(player) +
                    " position has at least one item, so he is not empty")
        elif choice == 7:
            clear()
            sys.exit()
        else:
            print("You must only select options 1 through 7")
            print("Please try again")

        input("\n\nEnter to continue: ")
        clear()

if __name__ == "__main__":
    # player dictionary template
    player = {'arrow': 0, 'dagger': 0, 'gold coin': 0, 'rope': 0, 'torch': 0}

    print("First you have to put your team:")
    team = insertion(player)
    menu(team, player)
