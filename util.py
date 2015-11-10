"""
File to put some utils functions
"""

def to_bin(number):
	return list(bin(number))[2:]

def to_int(binary):
	return int(''.join(v), 2)