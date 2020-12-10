#! /usr/bin/python3
from datetime import datetime, timedelta


class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def __iter__(self):
        return self.tasks.__iter__()

    def _add_task(self, task, **kwargs):
        self.tasks.append(task)

    def _add_new_task(self, description, **kwargs):
        self.tasks.append(Task(description, kwargs.get('dueDate', None)))

    def add(self, task, dueDate = None, **kwargs):
        chosenFunction = self._add_task if isinstance(task, Task) \
            else self._add_new_task
        kwargs['dueDate'] = dueDate
        chosenFunction(task, **kwargs)

    def pending(self):
        return [tasks for tasks in self.tasks if not tasks.done]

    def search(self, description):
        return [tasks for tasks in self.tasks if tasks.description == description][0]

    def __str__(self):
        return f'{self.name} ({len(self.pending())} pending task (s))'


class Task:
    def __init__(self, description, dueDate = None):
        self.description = description
        self.done = False
        self.creation = datetime.now()
        self.dueDate = dueDate

    def conclude(self):
        self.done = True

    def __str__(self):
        status = []
        if self.done:
            status.append(' (completed)')
        elif self.dueDate:
            if datetime.now() > self.dueDate:
                status.append(' (unsuccessful)')
            else: 
                days = (self.dueDate - datetime.now()).days
                status.append(f' (expires in {days} days)')

        return f'{self.description}'+ ''.join(status)

class RecurringTask(Task):
    def __init__(self, description, dueDate, days= 7):
        super().__init__(description, dueDate)
        self.days = days
    
    def conclude(self):
        super().conclude()
        new_dueDate = datetime.now() + timedelta(days=self.days)
        return RecurringTask(self.description, new_dueDate, self.days)

def main():
    house = Project('HOUSE TASKS')
    house.add('Ironing', datetime.now())
    house.add('wash the dishes', datetime.now() + timedelta(days= 3, minutes= 12))
    house.tasks.append(RecurringTask('make the bed', datetime.now(), 7))
    print(house)

    house.tasks.append(house.search('make the bed').conclude())
    print(house)

    house.search('wash the dishes').conclude()

    for tasks in house:
        print(f'- {tasks}')
    print(house)


if __name__ == '__main__':
    main()
