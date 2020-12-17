import datetime
import math


def print_help(command_collection, name_commands):
    print('There are {} commands in {} menu:'.format(len(command_collection), name_commands, ))

    for i in range(len(command_collection)):
        print("{}) {}".format(i, command_collection[i], ))


def print_collection_with_verify(items):
    if items is not None:
        print_collection(items)
    else:
        print('no find')


def choose_yes():
    print('(\'yes\'/any)')
    answer = input()
    return answer == 'yes'


def print_collection(items):
    print('list ({} elements): '.format(len(items), ))
    print('print collection?')
    if choose_yes():
        for item in items:
            print(item)
    else:
        print('good choice')


def enter_string():
    print('(string)')
    return input()


def enter_integer(min_value: int = 0, max_value: int = math.inf):
    while True:
        try:
            print("(integer)")
            value = int(input())
            if value < min_value or value > max_value:
                print("entered value is not correct")
                continue
            return value
        except Exception as e:
            print('entered value is not integer', e)
            continue


def enter_date():
    while True:
        try:
            print('(date in format YYYY-mm-dd)')
            date = datetime.datetime.strptime(input(), "%Y-%m-%d")
            return date
        except Exception as e:
            print('entered value is not date', e)
            continue


def enter_time():
    while True:
        try:
            print('(time in HH:MM format)')
            time = datetime.datetime.strptime(input(), "%H:%M")
            return time
        except Exception as e:
            print('entered value is not time', e)
            continue


def choose_output():
    print('Enter type of display: \n\'png\' to chart or any for console output')
    command = input()
    return command == 'png'


def choose_command(commands):
    print('print a number of command')
    for i in range(len(commands)):
        print(f'{i}. {commands[i]}')
    return enter_integer(0, len(commands)-1)
