#!/usr/bin/python3

from random import randint

def throw(kind_of_dice=6):
    return randint(1,kind_of_dice)

def kind_of_dice_computer():
    while True:
        kind_of_dice=randint(3,100)
        if kind_of_dice == 3 or kind_of_dice == 4 or kind_of_dice == 6 or kind_of_dice == 8 or kind_of_dice == 10 or kind_of_dice == 12 or kind_of_dice == 20 or kind_of_dice == 100:
            return kind_of_dice

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'