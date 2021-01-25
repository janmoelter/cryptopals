#!/usr/bin/python3

from library_functions import *


def parse_structured_string(_string):
	_structured_string = dict()

	if(re.fullmatch(r'^(?:[\w]+=[^=;]*;)*(?:[\w]+=[^=;]*)$', _string) != None):
		for _parameter in _string.split(';'):
			_k, _v = _parameter.split('=')
			_structured_string[_k] = _v

	return _structured_string

def submit_userdata(_string):
	for _r in [(';', '%3B'), ('=', '%3D')]:
		_string = _string.replace(_r[0], _r[1])

	return 'comment1=cooking%20MCs;userdata=' + _string + ';comment2=%20like%20a%20pound%20of%20bacon'

_key_bytes = random_bytes()
_iv_bytes = random_bytes()

def encrypt_userdata(_string):
	return CBC128_encryption(AES128_block_cipher, bytes_from_ascii(submit_userdata(_string)), _key_bytes, _iv_bytes)

def decrypt_userdata(_data_bytes):
	return parse_structured_string(print_as_ascii(CBC128_decryption(AES128_block_cipher, _data_bytes, _key_bytes)))

_decrypted_structured_string = decrypt_userdata(encrypt_userdata('12345'))



_success = 'admin' in _decrypted_structured_string and _decrypted_structured_string['admin'] == 'true'
print('Success: ', _success)
sys.exit(1)

#print('Output:\t', print_as_hex(_output))
#print('Output:\t', print_as_ascii(_output))

if(_success):
	sys.exit(0)
else:
	sys.exit(1)
