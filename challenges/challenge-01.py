#!/usr/bin/python3

from library_functions import *


_input = bytes_from_hex('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')

print('Input:\t', print_as_hex(_input))
print('Output:\t', print_as_base64(_input))

if('SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t' == print_as_base64(_input)):
	sys.exit(0)
else:
	sys.exit(1)
