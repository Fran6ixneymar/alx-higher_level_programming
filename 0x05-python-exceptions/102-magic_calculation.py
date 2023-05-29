#!/usr/bin/python3


def magic_calculation(a, b):
    result = 0
    for fig in range(1, 3):
        try:
            if fig > a:
                raise Exception('Too far')
            else:
                result += a ** b / fig
        except:
            result = b + a
            break
    return (result)
