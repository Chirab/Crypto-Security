#!/usr/bin/env python3
##
## EPITECH PROJECT, 2019
## break
## File description:
## key

import sys
import codecs
import re
import binascii
import os
import base64
from Crypto.Cipher import AES

def unpad(msg):
    return (msg[:-ord(msg[len(msg)-1:])])

def func_enc(msg1, msg2):
    try:
        clee = msg1
        var = AES.new(codecs.decode(clee, "hex"), AES.MODE_ECB)
        str = unpad(var.decrypt(base64.b64decode(msg2.strip())))
        str = base64.b64encode(str)
    except binascii.Error:
        exit(84)
    return(str)

def aes_ecb():
    tab = []
    if len(sys.argv) != 2:
        exit(84)
    if os.path.isfile(sys.argv[1]) == 0:
       exit(84)
    try:
        file = open(sys.argv[1], 'r')
        res = file.read()
        if res == "":
            exit(84)
        try:
            data = res.split('\n')
            for a in data:
                if len(a) is not 0:
                    tab.append(a)
            if len(tab) != 2:
                exit(84)
            str = func_enc(tab[0], tab[1])
            str = str.decode()
            print(str)
        except(ValueError, TypeError):
            exit(84)
    except FileNotFoundError:
            exit(84)

if __name__ == '__main__':
    aes_ecb()