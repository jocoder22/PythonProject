#!/usr/bin/env python


def addme(y):
    stop = False
    result = y + 10
    if result > 40:
        stop = True
    else:
        return result
    if stop:
        print('Number {} is greater than 40'.format(result))
