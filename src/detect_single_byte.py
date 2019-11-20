#!/usr/bin/env python3
##
## EPITECH PROJECT, 2019
## hex
## File description:
## xor
##

import sys
import binascii

def letter_score(a):
    resultat = []
    tab = {
        ' ': .13000,
        'a': .08167,
        'b': .01492,
        'c': .02782,
        'd': .04253,
        'e': .12702,
        'f': .02228,
        'g': .02015,
        'h': .06094,
        'i': .06094,
        'j': .00153,
        'k': .00772,
        'l': .04025,
        'm': .02406,
        'n': .06749,
        'o': .07507,
        'p': .01929,
        'q': .00095,
        'r': .05987,
        's': .06327,
        't': .09056,
        'u': .02758,
        'v': .00978,
        'w': .02360,
        'x': .00150,
        'y': .01974,
        'z': .00074
    }
    for byte in a.lower():
        char = chr(byte)
        res = tab.get(char, 0)
        resultat.append(res)
    return sum(resultat)

def xorvalue(string_byte, char):
    sorted = b''
    for byte in string_byte:
        sorted += bytes([byte ^ char])
    return sorted

def checkbyte(byte_string):
    liste = []
    newchain = []
    string_byte = bytes.fromhex(byte_string)
    for char in range(256):
        res = xorvalue(string_byte, char)
        key = letter_score(res)
        liste.append(key)
        final_res = max(liste)
        count = liste.index(max(liste))
    print(final_res, count)

def singlebyte():
    if len(sys.argv) != 2:
        exit(84)
    try:
        file = open(sys.argv[1], 'r')
        if file == "":
            exit(84)
        var = file.read().split('\n')
        if var == ['']:
            exit(84)
        for a in var:
            checkbyte(a)
        file.close()
    except FileNotFoundError:
        exit(84)

if __name__ == '__main__':
    singlebyte()