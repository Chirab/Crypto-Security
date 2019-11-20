#!/usr/bin/env python3
##
## EPITECH PROJECT, 2019
## hex
## File description:
## to base64
##

import sys
import codecs
import os
import base64
import string
import binascii

def hext_to_base():
    if len(sys.argv) != 2:
        exit(84)
    if os.path.isfile(sys.argv[1]) == 0:
       exit(84)
    try:
        file = open(sys.argv[1], 'r')
        res = file.read()
        if res == "":
            exit(84)
        res = res.replace('\n', '')
        try:
            b = codecs.decode(res, 'hex')
            base =  base64.b64encode(bytes.fromhex(res)).decode('utf-8')
            base = base.replace('\n', '')
            print(base)
        except binascii.Error:
            exit (84)
        file.close()
    except FileNotFoundError:
        exit(84)

if __name__ == '__main__':
    hext_to_base()

