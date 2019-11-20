#!/usr/bin/env python3
##
## EPITECH PROJECT, 2019
## hex
## File description:
## xor
##

import sys
import codecs
import binascii

def repeating_xor(msg, key):
    output_bytes = b''
    a = 0
    for byte in msg:
        output_bytes += bytes([byte ^ key[a]])
        if (a + 1) == len(key):
            a = 0
        else:
            a += 1
    return output_bytes.hex().upper()

def repeat_key():
    if len(sys.argv) != 2:
        exit (84)
    try:
        file = open(sys.argv[1], 'r')
        var1 = file.read()
        if var1 == "":
            exit(84)
        var = var1.split('\n')
        one = var[1]
        zero = var[0]
        if zero == "":
            exit(84)
        zer = bytes.fromhex(zero)
        on = bytes.fromhex(one)
        res = repeating_xor(on, zer)
        print(res)
    except FileNotFoundError:
        exit(84)

if __name__ == '__main__':
    repeat_key()