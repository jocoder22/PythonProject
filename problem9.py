#!/usr/bin/env python


def removeDupString(s):
    result = []

    seen = set()

    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)

    return ''.join(result)


print(removeDupString('babababadadamamayayameme'))
print(removeDupString('manamadada22'))


def removeDupList(lst):
    result = []

    seen = set()

    for char in lst:
        if char not in seen:
            seen.add(char)
            result.append(char)

    return result


print(removeDupList([9, 18, 29, 18, 9, 10, 10]))
print(removeDupList(['lit', 2, 4, 2, 3, 3, 3, 'lit', 'ma', 'lit', 'ma']))


