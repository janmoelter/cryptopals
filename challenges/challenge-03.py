#!/usr/bin/python3

from library_functions import *


_input = bytes_from_hex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')

_xor_b, _ = infer_xor_byte(_input)

_output = bytes_xor(_input, bytearray([_xor_b]))

print('Input:\t', print_as_hex(_input))
print('Output:\t', print_as_hex(_output))
print('Output:\t', print_as_ascii(_output))

if(bytes_from_hex('436f6f6b696e67204d432773206c696b65206120706f756e64206f66206261636f6e') == _output):
	sys.exit(0)
else:
	sys.exit(1)
