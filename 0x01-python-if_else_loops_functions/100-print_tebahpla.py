#!/usr/bin/python3
index = 0
for letter in range(122, 96, -1):
    print("{}".format(chr(letter - index)), end='')
    if index == 0:
        index = 32
    else:
        index = 0
