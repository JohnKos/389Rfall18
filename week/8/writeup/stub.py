#!/usr/bin/env python2

import sys
import struct


# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)


# Some constants. You shouldn't need to change these.
MAGIC = 0xdeadbeef
VERSION = 1

if len(sys.argv) < 2:
    sys.exit("Usage: python2 stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))

timestamp, author, sec_count = struct.unpack("<L8sL", data[8:24])

print("timestamp: %s" % (timestamp))
print("author: %s" % (author))
print("sections: %d" % (sec_count))

# We've parsed the magic and version out for you, but you're responsible for
# the rest of the header and the actual FPFF body. Good luck!

print("-------  BODY  -------")

i = 24
sec = 0

while sec < sec_count + 5:
	sec = sec + 1
	typ, length = struct.unpack("<LL", data[i:i+8])
	i = i + 8
	print("Section number %d" % (sec))
	print("Section type %d" % (typ))
	print("Section Length %d" % (length))
	if length > 0:
		if typ == 1:
			print("PNG")
			filename = "pngsection" + str(sec) + ".png"
			f = open(filename, 'w')
			f.write('\x89\x50\x4E\x47\x0D\x0A\x1A\x0A')
			f.write(data[i:i+length])
			i = i + length
		elif typ == 2:
			print("Double Word Array")
			dw = length/8
			inp = "<" + str(dw) + "Q"
			dat = struct.unpack(inp, data[i:i+length])
			print(dat)
			i = i + length
		elif typ == 3:
			print("Text")
			inp = "<" + str(length) + "s"
			text = struct.unpack(inp, data[i:i+length])
			print(text)
			i = i + length
		elif typ == 4:
			print("Double Array")
			doub = length/8
			inp = "<" + str(doub) + "d"
			dat = struct.unpack(inp, data[i:i+length])
			print(dat)
			i = i + length
		elif typ == 5:
			print("Word Array")
			words = length/4
			inp = "<" + str(words) + "L"
			dat = struct.unpack(inp, data[i:i+length])
			print(dat)
			i = i + length
		elif typ == 6:
			print("Coordinates")
			val1, val2 = struct.unpack("<dd", data[i:i+length])
			print(str(val1) + "  " + str(val2))
			i = i + length
		elif typ == 7:
			print("Section Reference")
			val = struct.unpack("<L", data[i:i+length])
			print("section referenced: " + str(val))
			i = i + length
		elif typ == 9:
			print("Text")
			inp = "<" + str(length) + "s"
			text = struct.unpack(inp, data[i:i+length])
			print(text)
			i = i + length
		else:
			print("type mismatch")


