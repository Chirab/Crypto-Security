#!/usr/bin/env python3
##
## EPITECH PROJECT, 2019
## xor
## File description:
## fixed
##

import sys
import os.path
import codecs

def check_len():
    if len(sys.argv) != 2:
        exit(84)
    if os.path.isfile(sys.argv[1]) == 0:
       exit(84)
    try:
        file = open(sys.argv[1], 'r')
        first = file.readlines()
        if first == "":
            exit(84)
        if len(first) != 2:
            exit(84)
        Fline = first[0]
        Sline = first[1]
        number1 = len(Fline)
        number2 = len(Sline)
        if number1 != number2:
            exit(84)
        else:
            try:
                finalRes = hex(int(Fline, 16) ^ int(Sline, 16))[2:]
                print(finalRes.upper())
            except:
                exit(84)
        file.close()
    except FileNotFoundError:
        exit(84)


if __name__ == '__main__':
    check_len()