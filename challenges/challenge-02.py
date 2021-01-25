#!/usr/bin/python3

from library_functions import *


_input = [ bytes_from_hex('1c0111001f010100061a024b53535009181c'), bytes_from_hex('686974207468652062756c6c277320657965') ]

_output = bytes_xor(_input[0], _input[1])

print('Input:\t', print_as_hex(_input[0]))
print('Input:\t', print_as_hex(_input[1]))
print('Output:\t', print_as_hex(_output))

if(bytes_from_hex('746865206b696420646f6e277420706c6179') == _output):
	sys.exit(0)
else:
	sys.exit(1)
