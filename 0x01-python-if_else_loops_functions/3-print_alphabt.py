#!/usr/bin/python3
for P in range(97, 123):
    if chr(P) is not 'q' and chr(P) is not 'e':
        continue
        print(chr(P).format(P), end="")
