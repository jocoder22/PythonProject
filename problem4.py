#!/usr/bin/env python

from random import randint


def dice7():
    return randint(1, 7)


def convert7to5():
    roll = 7

    while roll > 5:
        roll = dice7()
        print('dice7() produced a roll of', roll)
    print(' Your final returned roll is below:')
    return roll

