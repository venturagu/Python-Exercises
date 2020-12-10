#! /usr/bin/python3
from datetime import datetime

class Task:
    def __init__(self, description):
        self.description = description
        self.done = False
        self.creation = datetime.now()

    def conclude(self):
        self.done = True

    def __str__(self):
        return self.description + ('(Done)' if self.done else '')

def main():
        house = []
        house.append(Task('Ironing'))
        house.append(Task('wash the dishes'))

        [task.conclude() for task in house if task.description == 'wash the dishes']
        for task in house:
            print(f'- {task}')

if __name__ == '__main__':
    main()

       