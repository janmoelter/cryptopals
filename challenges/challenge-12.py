#!/usr/bin/python3

from library_functions import *


_input = bytes_from_base64('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK')

_key_bytes = random_bytes()

def encryption_oracle(_bytes):
	_unknown_bytes = _input
	return ECB128_encryption(AES128_block_cipher, _bytes + _unknown_bytes, _key_bytes)


_block_length = detect_encryption_block_length(encryption_oracle)
#print('Block length: ', _block_length)
_ebc_mode = detect_ecb_encryption(encryption_oracle, _block_length=_block_length)
#print('EBC encryption: ', _ebc_mode)
if not _ebc_mode: sys.exit(1)


_0_padded_enc_bytes = dict()
for n in range(_block_length):
	_0_padded_enc_bytes[n] = encryption_oracle(bytearray(n))

for n in range(_block_length - 1):
	if len(_0_padded_enc_bytes[n]) < len(_0_padded_enc_bytes[n+1]):
		_number_unknown_bytes = (len(_0_padded_enc_bytes[0]) // _block_length)*_block_length - (n+1)
		break

_output = bytearray()
for n in range(_number_unknown_bytes):
	_match = False

	_N_blocks = n // _block_length + 1

	_0_test_bytes = bytearray(_block_length - n % _block_length - 1)
	_test_bytes = _0_test_bytes + _output[:n]

	for x in range(256):
		_x_byte = bytearray([x])
		if encryption_oracle(_test_bytes + _x_byte)[:_N_blocks*_block_length] == _0_padded_enc_bytes[len(_0_test_bytes)][:_N_blocks*_block_length]:
			_output = _output + _x_byte
			_match = True
			break


print('Input:\t', print_as_hex(_input))
print('Output:\t', print_as_hex(_output))
print('Output:\t', print_as_ascii(_output))

if(_input == _output):
	sys.exit(0)
else:
	sys.exit(1)
