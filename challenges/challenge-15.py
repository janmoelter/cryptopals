#!/usr/bin/python3

from library_functions import *


_input = b'ICE ICE BABY\x04\x04\x04\x04'


_output = remove_PKCS7_padding(_input)

print('Output:\t', print_as_hex(b'ICE ICE BABY'))
#print('Output:\t', print_as_ascii(_output))

if(bytes_from_hex('494345204943452042414259') == _output):
	sys.exit(0)
else:
	sys.exit(1)
