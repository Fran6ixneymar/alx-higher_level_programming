#!/usr/bin/python3


def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    if a < b:
        total = add(a, b)
        for fig in range(4, 6):
            total = add(total, fig)
        return (total)

    else:
        return(sub(a, b))
