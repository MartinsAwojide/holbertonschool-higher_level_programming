#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if (ord(c) > 96) and (ord(c) < 123):
            up = ord(c) - 32
        else:
            up = ord(c)
        print('{}'.format(chr(up)), end='')
    print()
