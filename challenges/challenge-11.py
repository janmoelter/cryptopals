#!/usr/bin/python3

from library_functions import *


def encryption_oracle(_bytes):
	_key_bytes = random_bytes()

	_bytes = random_bytes(length=random.randint(5, 10)) + _bytes + random_bytes(length=random.randint(5, 10))

	if(random.randint(0, 1)):
		_enc_mode = 'CBC'
		_enc_bytes = CBC128_encryption(AES128_block_cipher, _bytes, _key_bytes, random_bytes())
		_enc_bytes = _enc_bytes[16:]
	else:
		_enc_mode = 'ECB'
		_enc_bytes = ECB128_encryption(AES128_block_cipher, _bytes, _key_bytes)

	return _enc_bytes, _enc_mode


_input = bytearray(3*16)

_success = True
for _ in range(50):
	_enc_input, _enc_mode = encryption_oracle(_input)
	
	if(_enc_mode != ['CBC', 'ECB'][detect_repeating_block(_enc_input)]):
		_success = False
		break

#print('Output:\t', print_as_hex(_output))
#print('Output:\t', print_as_ascii(_output))

if(_success):
	sys.exit(0)
else:
	sys.exit(1)
