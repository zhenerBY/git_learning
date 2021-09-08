from datetime import datetime
from datetime import date
from datetime import timedelta

def welcome_scr():
    print('|----------------------------------------------------------------|')
    print('|                     LIST OF TASKS                              |')
    print('|----------------------------------------------------------------|')
    print('| 1 - Show tasks list                                            |')
    print('| 2 - Add task                                                   |')
    print('| 3 - Edit task                                                  |')
    print('| 4 - Rename task                                                |')
    print('| 5 - Delete task                                                |')
    print('|----------------------------------------------------------------|')
    print('|----------------------------------------------------------------|')
    print('|----------------------------------------------------------------|')
    print('|----------------------------------------------------------------|')
    print('|----------------------------------------------------------------|')
    print('| exit - Exit the programm                                       |')
    print('|----------------------------------------------------------------|')


task_att = ('description', 'created', 'deadline')
task_dict = {
             'Test Task 1': {'description': 'Очень важная задача',
                             'created': date(2021, 9, 8), 'deadline': date(2021, 9, 9)},
             'Test Task 2': {'description': 'Очень важная задача2',
                             'created': date(2021, 8, 8), 'deadline': date(2021, 8, 9)},
             'Test Task 3': {'description': 'Очень важная задача3',
                             'created': date(2021, 8, 8), 'deadline': date(2021, 10, 10)}
             }

action = 0
while action != 'exit' and action != 'Exit':
    welcome_scr()
    action = input()
    if action == '1':
        for c1, tsk in enumerate(task_dict):
            print(f'Task #{c1 + 1} - {tsk}')
        input('Press Enter to continue')
    if action == '2':
        name_tmp = input('Enter name of new task :')
        task_tmp = {}
        flag = True
        while flag:
            for att in task_att:
                if att == 'created':
                    task_tmp[att] = date.today()
                elif att == 'deadline':
                    task_tmp[att] = task_tmp['created'] + timedelta(days = int(input('Enter number of days required to complete the task')))
                else:
                    task_tmp[att] = input(f'Enter task {att} :')
            print('This is correct? ')
            print(f'Task name - {name_tmp}')
            aaa='description'
            print(f'Discription - {task_tmp[aaa]}')


        task_dict[name_tmp] = task_tmp
    elif action == 'exit' or action == 'Exit':
        None
    else:
        print('Incorrect input. Repeat.')

        # print('Nothing happens')
