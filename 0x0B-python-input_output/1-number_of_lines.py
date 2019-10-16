#!/usr/bin/python3


def number_of_lines(filename=""):
    """returns number of line in a text file"""
    with open(filename, encoding="utf-8") as myFile:

        lineNum = 0

        while True:

            line = myFile.readline()
            if not line:
                break
            lineNum += 1
    return lineNum
