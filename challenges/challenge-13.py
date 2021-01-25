#!/usr/bin/python3

from library_functions import *


def parse_structured_cookie(_string):
	_structured_cookie = dict()

	#if(re.fullmatch(r'^(?:[\w]+=[^\s\n=&]+&)*(?:[\w]+=[^\s\n=&]+)$', _string) != None):
	if(re.fullmatch(r'^(?:[\w]+=[^=&]+&)*(?:[\w]+=[^=&]+)$', _string) != None):
		for _parameter in _string.split('&'):
			_k, _v = _parameter.split('=')
			_structured_cookie[_k] = _v

	return _structured_cookie

def profile_for(_email):
	#if(re.fullmatch(r'^[\w\d\.\-_]+@[\w\d\.\-_]+\.[\w]{1,3}$', _email) != None):
	if(re.fullmatch(r'^[^&=]+@[^&=]+\.[^&=]{1,3}$', _email) != None):
		_uid = 10
		_role = 'user'

		return str('email=' + _email + '&uid=' + str(_uid) + '&role=' + _role)

_key_bytes = random_bytes()

def encrypted_profile_for(_email):
	return ECB128_encryption(AES128_block_cipher, bytes_from_ascii(profile_for(_email)), _key_bytes)

def decrypt_profile(_profile_bytes):
	return parse_structured_cookie(print_as_ascii(ECB128_decryption(AES128_block_cipher, _profile_bytes, _key_bytes)))


_test_email = b'__________admin\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b@myserver.com'.decode('ascii')
_injection_block = encrypted_profile_for(_test_email)[16:32]

_enc_forged_profile = encrypted_profile_for('this-is-an-admin@myserver.com')
_enc_forged_profile[48:64] = _injection_block


_forged_profile = decrypt_profile(_enc_forged_profile)

print(_forged_profile)

_success = (_forged_profile['role'] == 'admin')


#print('Output:\t', print_as_hex(_output))
#print('Output:\t', print_as_ascii(_output))

if(_success):
	sys.exit(0)
else:
	sys.exit(1)
