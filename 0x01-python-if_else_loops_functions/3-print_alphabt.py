#!/usr/bin/python3
for P in range(97, 123):
    if chr(P) == 'q' or chr(P) == 'e':
        continue
    print(chr(P).format(P), end='')
