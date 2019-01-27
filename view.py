#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dao import persondao
from model import person
from util import is_empty
import os
from platform   import system as system_name  # Returns the system/OS name


__NO_PERSON = "There is no person."

def start(show_menu=True):
    clear_screen()
    print('Person - Python MongoDB (PyMongo)\n')
    if show_menu:
        return menu()

def menu():
    print('1 - Insert person')
    print('2 - List registered people')
    print('3 - Find person by id')
    print('4 - Find person by name')
    print('5 - Delete person')
    print('6 - Update person')
    print('7 - Count registered people')
    print('8 - Delete all')
    print('0 - Exit')
    return input('\nOption: ')

def invalid_option():
    print('Invalid option.')

def get_person(_id=None, p=None):
    if p is not None:
        newp = p
        print('\n\nEnter new person data\n(Note: Leave empty the fields you want to keep the same value.)\n')
    else:
        newp = person(_id=_id)
        print('Enter person data\n')
    newp.name = input('Name: ').strip()
    age = input('Age: ').strip()
    newp.age = float(age) if not is_empty(age) else None
    newp.gender = input('Gender: ').strip()
    return newp

def get_id():
    _id = input('Person ID: ')
    return _id if _id.isnumeric() else -1

def get_name():
    return input('Name: ')

def print_person(p):
    if p is not None:
        print(f'\nID: {p._id}\nName: {p.name}\nAge: {p.age}\nGender: {p.gender}')
        return True
    print(f'\n{__NO_PERSON}')
    return False

def print_people(people, br=False):
    if br:
        print()
    if len(people) == 0:
        print(f'{__NO_PERSON}')
    else:
        for p in people:
            print(f' {p._id} - {p.name}')

def print_count(count):
    print(f'There are {count} people registered.' if count > 1 else 'There is one person registered.' if count is 1 else __NO_PERSON)

def confirm_drop():
    return input('Are you sure to delete all registered people? (Y/N): ').lower().startswith('y')

def confirm_delete():
    return input('\nAre you sure to delete this person? (Y/N): ').lower().startswith('y')

def clear_screen():
    '''Clears the terminal screen.'''
    os.system('cls' if system_name().lower()=='windows' else 'clear')

def pause():
    input('\nPress ENTER to continue...')

def exit():
    print('\nBye!')
