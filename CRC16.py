def xor(a, b):
	result = []
	
	for i in range(1, len(b)):
		if a[i] == b[i]:
			result.append('0')
		else:
			result.append('1')

	return ''.join(result)


def mod2div(dividend, divisor):
	length = len(divisor)
	tmp = dividend[0 : length]

	while length < len(dividend):
		if tmp[0] == '1':
			tmp = xor(divisor, tmp) + dividend[length]

		else:
			tmp = xor('0'*length, tmp) + dividend[length]

		length += 1

	if tmp[0] == '1':
		tmp = xor(divisor, tmp)
	else:
		tmp = xor('0'*length, tmp)

	checkword = tmp
	return checkword


def encodeData(data, key):
	keyLength = len(key)

	appended_data = data + '0'*(keyLength-1)
	remainder = mod2div(appended_data, key)

	codeword = data + remainder
	print("Remainder of mod2 division is : ", remainder)
	print("Encoded Data (Data + Remainder) : ",
		codeword)
		
		
def decodeData(edata, key):
	l_key = len(key)

	appended_data = edata + '0'*(l_key-1)
	remainder = mod2div(appended_data, key)

	codeword = edata + remainder
	print("Remainder of mod2 division is : ", remainder)
	print("Decoded Data (Data + Remainder) : ",
		codeword)


# Driver code
data = input("Enter the dataword : ")
key = input("Enter the generator : ")
encodedData = encodeData(data, key)
decodeData(encodedData, key)
