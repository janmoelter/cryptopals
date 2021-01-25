#!/usr/bin/python3

from library_functions import *


_input_file = open('data/4.txt', 'r')
_input = [bytes_from_hex(line.strip()) for line in _input_file]
_input_file.close()


_inferred_xor_b = [infer_xor_byte(_input[i]) for i in range(len(_input))]
_, _i = minimum([s for _, s in _inferred_xor_b])
_xor_b, _ = _inferred_xor_b[_i]


_output = bytes_xor(_input[_i], bytearray([_xor_b]))

print('Output:\t', print_as_hex(_output))
print('Output:\t', print_as_ascii(_output))

if(bytes_from_hex('4e6f77207468617420746865207061727479206973206a756d70696e670a') == _output):
	sys.exit(0)
else:
	sys.exit(1)
