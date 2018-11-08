#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
import hashlib
import string

# this will work if you place this script in your writeup folder
words = []
with open("../probable-v2-top1575.txt", 'r') as wordlist:
	for line in wordlist:
		for insert in line.split():
			words.append(insert)

hashes = []
with open("../hashes","r") as hashlist:
	for line in hashlist:
		for insert in line.split():
			hashes.append(insert)


# a string equal to 'abcdefghijklmnopqrstuvwxyz'.
salts = string.ascii_lowercase


for salt in salts:
    for word in words:
	val = salt + word
	out = hashlib.sha512((val)).hexdigest()
	out = str(out)
	for ha in hashes:
		if (ha == out):
			print("salt: " + salt + "   word: " + word)

