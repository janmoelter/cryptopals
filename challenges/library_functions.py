
import sys
import subprocess
import base64

import random
import secrets

from Crypto.Cipher import AES

from statistics import mean

import re


# Challenge 1

def bytes_from_hex(_string):
	return bytearray.fromhex(_string)

def bytes_from_base64(_string):
	return base64.b64decode(_string)

def print_as_base64(_bytes):
	return base64.b64encode(_bytes).decode('ascii')

def print_as_hex(_bytes):
	return _bytes.hex()

# Challenge 2

def bytes_xor(_bytes, _xor_bytes):
	return bytearray([_bytes[i] ^ _xor_bytes[i % len(_xor_bytes)] for i in range(len(_bytes))])

# Challenge 3

def byte_frequency_score(_bytes, reject_non_printable=True):
	letter_bytes = {
		"a": [ord('a'), ord('A')],
		"b": [ord('b'), ord('B')],
		"c": [ord('c'), ord('C')],
		"d": [ord('d'), ord('D')],
		"e": [ord('e'), ord('E')],
		"f": [ord('f'), ord('F')],
		"g": [ord('g'), ord('G')],
		"h": [ord('h'), ord('H')],
		"i": [ord('i'), ord('I')],
		"j": [ord('j'), ord('J')],
		"k": [ord('k'), ord('K')],
		"l": [ord('l'), ord('L')],
		"m": [ord('m'), ord('M')],
		"n": [ord('n'), ord('N')],
		"o": [ord('o'), ord('O')],
		"p": [ord('p'), ord('P')],
		"q": [ord('q'), ord('Q')],
		"r": [ord('r'), ord('R')],
		"s": [ord('s'), ord('S')],
		"t": [ord('t'), ord('T')],
		"u": [ord('u'), ord('U')],
		"v": [ord('v'), ord('V')],
		"w": [ord('w'), ord('W')],
		"x": [ord('x'), ord('X')],
		"y": [ord('y'), ord('Y')],
		"z": [ord('z'), ord('Z')],
		"*": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 91, 92, 93, 94, 95, 96, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255]
	}
	EN_letter_frequency = {
		"a": 0.08167,
		"b": 0.01492,
		"c": 0.02782,
		"d": 0.04253,
		"e": 0.12702,
		"f": 0.02228,
		"g": 0.02015,
		"h": 0.06094,
		"i": 0.06966,
		"j": 0.00153,
		"k": 0.00772,
		"l": 0.04025,
		"m": 0.02406,
		"n": 0.06749,
		"o": 0.07507,
		"p": 0.01929,
		"q": 0.00095,
		"r": 0.05987,
		"s": 0.06327,
		"t": 0.09056,
		"u": 0.02758,
		"v": 0.00978,
		"w": 0.02360,
		"x": 0.00150,
		"y": 0.01974,
		"z": 0.00074,
		"*": 0.00001
	}

	if(reject_non_printable):
		for x in _bytes:
			if(x not in [10, 13, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126]):
				return float('inf')
	
	N = len(_bytes)
	chi2score = 0

	for c in EN_letter_frequency.keys():
		Nc = sum([_bytes.count(x) for x in letter_bytes[c]])
		chi2score += (Nc - N * EN_letter_frequency[c])**2 / (N * EN_letter_frequency[c])
	
	return chi2score

def minimum(_list):
	return min((_value, _index) for (_index, _value) in enumerate(_list))

def infer_xor_byte(_bytes, reject_non_printable=True):
	_frequency_score, _xor_b = minimum([byte_frequency_score(bytes_xor(_bytes, bytearray([xor_b])), reject_non_printable=reject_non_printable) for xor_b in range(256)])
	return (_xor_b, _frequency_score)

# Challenge 5

def bytes_from_ascii(_string):
	return bytearray(_string, 'ascii')

# Challenge 6

def hamming_distance(_bytes_1, _bytes_2):
	assert len(_bytes_1) == len(_bytes_2)

	_xor_bytes = bytes_xor(_bytes_1, _bytes_2)
	return sum([sum([(x >> n) & 1 for n in range(8)]) for x in _xor_bytes])

# Challenge 7

def AES128_block_cipher(_bytes, _key_bytes, decrypt=False):
	#_shell_process = subprocess.Popen(' '.join(['openssl enc -aes-128-ecb', ['-e', '-d'][decrypt], '-nosalt -nopad -K' , print_as_hex(_key_bytes)]), stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
	#
	#_shell_process.stdin.write(_bytes)
	#(stdout_data, stderr_data) =_shell_process.communicate()
	#_shell_process.stdin.close()
	#
	#if(_shell_process.returncode == 0):
	#	return stdout_data
	#else:
	#	return bytearray([])
	#
	aes = AES.new(bytes(_key_bytes), AES.MODE_ECB)
	if not decrypt:
		return aes.encrypt(bytes(_bytes))
	else:
		return aes.decrypt(bytes(_bytes))

def ECB128_encryption(block_cipher, _bytes, _key_bytes):
	_bytes = add_PKCS7_padding(_bytes, block_length=16)

	_output = bytearray()
	for i in range(len(_bytes) // 16):
		_output += block_cipher(_bytes[i*16:(i+1)*16], _key_bytes)

	return _output

def ECB128_decryption(block_cipher, _bytes, _key_bytes):

	_output = bytearray()
	for i in range(len(_bytes) // 16):
		_output += block_cipher(_bytes[i*16:(i+1)*16], _key_bytes, decrypt=True)

	_output = remove_PKCS7_padding(_output, block_length=16)

	return _output

# Challenge 9

def add_PKCS7_padding(_bytes, block_length=16):
	n_p = block_length - len(_bytes) % block_length
	return _bytes + bytearray([n_p for _ in range(n_p)])

# Challenge 10

def CBC128_encryption(block_cipher, _bytes, _key_bytes, _iv_bytes):

	_bytes = add_PKCS7_padding(_bytes, block_length=16)

	_output = _iv_bytes[:]
	for i in range(len(_bytes) // 16):
		_output += block_cipher(bytes_xor(_output[i*16:(i+1)*16], _bytes[i*16:(i+1)*16]), _key_bytes)

	return _output

def CBC128_decryption(block_cipher, _bytes, _key_bytes):

	_output = bytearray()
	for i in reversed(range(1, len(_bytes) // 16)):
		_output = bytes_xor(block_cipher(_bytes[i*16:(i+1)*16], _key_bytes, decrypt=True), _bytes[(i-1)*16:i*16]) + _output

	_output = remove_PKCS7_padding(_output, block_length=16)

	return _output

# Challenge 11

def random_bytes(length=16):
	return bytearray(secrets.token_bytes(nbytes=length))

def detect_repeating_block(_bytes, _block_length=16):
	for i in range(len(_bytes)-16):
		for j in range(len(_bytes)-2*16-i):
			if(_bytes[i:i+16] == _bytes[i+16+j:i+16+j+16]):
				return True
	
	return False

# Challenge 12

def detect_encryption_block_length(_encryption_oracle):
	n = 0
	_block_length = 0
	while(_block_length == 0):
		n += 1
		_block_length = len(_encryption_oracle(bytearray(n+1))) - len(_encryption_oracle(bytearray(n)))

	return _block_length

def detect_ecb_encryption(_encryption_oracle, _block_length=16):
	_enc_bytes = _encryption_oracle(bytearray(3*_block_length))
	return detect_repeating_block(_enc_bytes)

# Challenge 13

def print_as_ascii(_bytes):
	def ascii_chr(_x):
		if _x in [9, 10, 13, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126]:
			return chr(_x)
		else:
			return '�'
	
	return ''.join([ascii_chr(_x) for _x in _bytes])
	#return _bytes.decode('ascii')

# Challenge 15

def remove_PKCS7_padding(_bytes, block_length=16):
	assert len(_bytes) > 0
	assert len(_bytes) % block_length == 0

	n_p = _bytes[-1]
	if n_p <= block_length and _bytes[-n_p:] == bytearray([n_p for _ in range(n_p)]):
		return _bytes[:-n_p]
	else:
		raise Exception('Bad PKCS#7 padding.')
