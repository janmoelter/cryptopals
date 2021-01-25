#!/usr/bin/python3

from library_functions import *


_input_file = open('data/8.txt', 'r')
_input = [bytes_from_hex(line.strip()) for line in _input_file]
_input_file.close()

for _input_line in _input:
	for i in range(len(_input_line) // 16):
		if(any([_input_line[i*16:(i+1)*16] == _input_line[n*16:(n+1)*16] for n in range(i+1,len(_input_line) // 16)])):
			_output = _input_line
			break


print('Output:\t', print_as_hex(_output))
#print('Output:\t', print_as_ascii(_output))

if(bytes_from_hex('d880619740a8a19b7840a8a31c810a3d08649af70dc06f4fd5d2d69c744cd283e2dd052f6b641dbf9d11b0348542bb5708649af70dc06f4fd5d2d69c744cd2839475c9dfdbc1d46597949d9c7e82bf5a08649af70dc06f4fd5d2d69c744cd28397a93eab8d6aecd566489154789a6b0308649af70dc06f4fd5d2d69c744cd283d403180c98c8f6db1f2a3f9c4040deb0ab51b29933f2c123c58386b06fba186a') == _output):
	sys.exit(0)
else:
	sys.exit(1)
