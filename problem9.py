#!/usr/bin/env python


def removeDup(lst):
    result = []

    seen = set()

    for char in lst:
        if char not in seen:
            seen.add(char)
            result.append(char)

    return ''.join(result)


print(removeDup('babababadadamamayayameme'))
