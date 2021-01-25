#!/usr/bin/python3

from library_functions import *


_input = bytes_from_ascii('Burning \'em, if you ain\'t quick and nimble\nI go crazy when I hear a cymbal')

_output = bytes_xor(_input, bytes_from_ascii('ICE'))

print('Input:\t', print_as_hex(_input))
print('Output:\t', print_as_hex(_output))

if(bytes_from_hex('0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f') == _output):
	sys.exit(0)
else:
	sys.exit(1)
