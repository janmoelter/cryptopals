#!/usr/bin/python3

from library_functions import *


_input = bytes_from_ascii('YELLOW SUBMARINE')


_output = add_PKCS7_padding(_input, block_length=20)

print('Output:\t', print_as_hex(_output))
#print('Output:\t', print_as_ascii(_output))

if(bytes_from_hex('59454c4c4f57205355424d4152494e4504040404') == _output):
	sys.exit(0)
else:
	sys.exit(1)
