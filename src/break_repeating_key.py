#!/usr/bin/env python3
##
## EPITECH PROJECT, 2019
## break
## File description:
## key

import sys

def hamming_distance(s1, s2):
	res = ''.join(format(ord(i), 'b') for i in s1)
	res1 = ''.join(format(ord(i), 'b') for i in s2)
	var = str(res)
	var1 = str(res1)
	if len(var) == len(var1):
		return sum(ch1 != ch2 for ch1, ch2 in zip(var, var1))
	else:
		exit(84)
 
def break_rep():
	file = open(sys.argv[1], 'r')
	res = file.read()
	print(res)

if __name__ == '__main__':
    a = 'Hello'
    b = 'World'
    c = hamming_distance(a, b)
    print(c)