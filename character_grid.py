#! /usr/bin/python3


import sys
from os import system, name


# complete grid
grid =  [['.', '.', '.', '.', '.', '.',' ', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '0', '0', '.', '.', '.',' ', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
         ['0', '0', '0', '0', '.', '.',' ', '.', '.', '0', '0', '.', '0', '0', '.', '.'],
         ['0', '0', '0', '0', '0', '.',' ', '.', '0', '0', '0', '.', '0', '0', '0', '.'],
         ['.', '0', '0', '0', '0', '0',' ', '.', '0', '0', '0', '.', '0', '0', '0', '.'],
         ['0', '0', '0', '0', '0', '.',' ', '.', '.', '0', '0', '0', '0', '0', '.', '.'],
         ['0', '0', '0', '0', '.', '.',' ', '.', '.', '.', '0', '0', '0', '.', '.', '.'],
         ['.', '0', '0', '.', '.', '.',' ', '.', '.', '.', '.', '0', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.',' ', '.', '.', '.', '.', '.', '.', '.', '.', '.']]

# Horizontal grid
grid_a =   [['.', '.', '.', '.', '.', '.'],
            ['.', '0', '0', '.', '.', '.'],
            ['0', '0', '0', '0', '.', '.'],
            ['0', '0', '0', '0', '0', '.'],
            ['.', '0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0', '.'],
            ['0', '0', '0', '0', '.', '.'],
            ['.', '0', '0', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]
            
# vertical grid
grid_b =   [['.', '.', '0', '0', '.', '0', '0', '.', '.'],
            ['.', '0', '0', '0', '.', '0', '0', '0', '.'],
            ['.', '0', '0', '0', '.', '0', '0', '0', '.'],
            ['.', '.', '0', '0', '0', '0', '0', '.', '.'],
            ['.', '.', '.', '0', '0', '0', '.', '.', '.'],
            ['.', '.', '.', '.', '0', '.', '.', '.', '.']]

            
# Change grid orientation
def changeOrientation(grid):
    for y in range(len(grid[0])):
        for x in range(len(grid)):
            if(grid[x][y] == '0'):
                print("\033[1;36m"+grid[x][y]+"\033[m", end='')
            else:
                print("\033[1;31;40m"+grid[x][y]+"\033[m", end='')
        print()


# define a clear function
def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# Break or continue a flow


def exitOrContinue():
    print("Do you want to go out? (Y) yes to exit or any key to continue")
    option = input().upper()
    if(option == 'Y'):
        sys.exit()
    else:
        clear()
        return


def menu(grid, grid_a, grid_b):
    while True:
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                print("\033[1;36;40m"+grid[y][x]+"\033[m", end='')
            print()

        print("\nWhich heart do you want to change the orientation?\n\n\
1 - Change the orientation of the right heart,\n\
2 - Change the orientation of the left heart.\n\
3 - Change the orientation of two hearts.\n\
4 - exit.\n")
        option = input().upper()
        if(option == '1'):
            print()
            changeOrientation(grid_a)
            exitOrContinue()
        elif((option.upper() == '2')):
            print()
            changeOrientation(grid_b)
            exitOrContinue()
        elif((option.upper() == '3')):
            print()
            changeOrientation(grid)
            exitOrContinue()
        elif((option.upper() == '4')):
            sys.exit()
        else:
            exitOrContinue()


menu(grid, grid_a, grid_b)
