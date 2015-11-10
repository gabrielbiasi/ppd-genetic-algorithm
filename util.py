"""
File to put some utils functions
"""

def to_bin(number):
	return list(bin(number))[2:]

def to_int(binary):
	return int(''.join(v), 2)

def individualEquals(ind1, ind2):
	if len(ind1) != len(ind2):
		raise Exception('The chromossomes have different sizes!')

	eq = 0
	size = len(ind1)
	for x, y in zip(ind1, ind2):
		if x == y:
			eq += 1
	
	return (float(eq) / size)
