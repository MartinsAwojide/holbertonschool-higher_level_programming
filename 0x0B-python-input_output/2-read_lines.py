#!/usr/bin/python3


def read_lines(filename="", nb_lines=0):
    """reads n lines of a text file"""
    with open(filename, encoding="utf-8") as myFile:

        lineNum = 0

        while True:

            line = myFile.readline()
            if not line or (lineNum >= nb_lines and nb_lines > 0):
                break
            lineNum += 1
            print(line, end='')
