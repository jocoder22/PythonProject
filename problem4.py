#!/usr/bin/env python

from random import randint


def dice7():
    return randint(1, 7)


def convert7to5():
    roll = 7

    while roll > 5:
        roll = dice7()
        print('dice7() produced a roll of', roll)
    print('    Your final returned roll is below:')
    return roll


def dice5():
    randint(1, 5)


def convert5to7():
    while True:
        roll_1 = dice5()
        roll_2 = dice5()

        num = ((roll_1 - 1) * 5)  + roll_2

        if num > 21:
            continue

        return num %7 + 1

        
convert7to5()
