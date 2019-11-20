#!/usr/bin/env python3
##
## EPITECH PROJECT, 2019
## break
## File description:
## key

import sys

def detect_aes():
    if len(sys.argv) != 2:
        exit(84)
    file = open(sys.argv[1], 'r')
    var = file.read()
    if var == "":
        exit(84)

if __name__ == '__main__':
    detect_aes()