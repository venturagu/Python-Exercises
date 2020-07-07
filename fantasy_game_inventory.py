"""The challenge is construct a script to a fantasy game inventory wich be have follows features:

1. Insert players into a team
2. Item count (total and specific element)
3. Team average and player average
4. Highest and lowest average score on the team
5. Highest and lowest average score per item
6. filter if a player has the same number as another player for a specific item
7. filter if a player has at least one item

The focus is on practicing how to use the dictionary and list data structure for problem solving
"""

import pprint
import copy
from os import system, name
import time

# player dictionary template
player = {'arrow': 0, 'dagger': 0, 'gold coin': 0, 'rope': 0, 'torch': 0}


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
            time.sleep(1)  # Sleep for 1 seconds
            clear()
            continue
        break

    pprint.pprint(gamers_list)


insertion(player)
