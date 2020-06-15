
class AR14:
	def __init__(self):
		self.var1 = "1000011001011011" 
		self.var2 = "1000101110001100" 
		self.var3 = "1110001011010010" 
		self.var4 = "0111000001110101" 
		self.var5 = "1111101100011111" 
		self.var6 = "1010011011100110" 
		self.var7 = "0000010111001010" 
		self.var8 = "0111111100000010" 
		# Stores 8 binary variables
		
		self.xor = self.var1 + self.var2 + self.var3 + self.var4 + self.var5 + self.var6 + self.var7 + self.var8


	'''
		textBin('text') transform the parameter to binary

	'''


	def textBin(self, a):
		den = [] # A denary array to store the denary value of the text
		binn = [] # A binary array to store the binary value of the text
		
		# This loop basically just converts one character of the text to denary via ASCII coding and appends it in denary array
		for c in range(len(a)):
			den.append(ord(a[c]))

		# This loop loops through the denary array and appends it into the binary array
		for d in range(len(den)):
			binn.append(format(den[d], 'b'))

		# The result varible transform the binary array into a string
		result = ''.join(binn)

		# Then the result variable splits the string into array with each char with its own index
		result = list(result)

		return result


	'''
		xorGate(0,1)- takes two input and returns a xor function's result
	'''
	def xorGate(self, input1, input2):
		input1 = int(input1)
		input2 = int(input2)
		summ = input1 + input2
		if summ == 1:
			return '1'
		else:
			return '0'


	'''
		binToHex('0101')- takes a binary input in the form of string and returns hex in the form of string
	'''
	def binToHex(self, inputt):
		hex_val = '0123456789abcdef'
		bin_val = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
		currentIndex = 0
		delimiter = 0
		currentValue = ''
		finalArr = []

		for x in range(len(inputt)):
			currentValue = currentValue + inputt[x]
			delimiter = delimiter + 1
			if delimiter == 4:
				finalArr.append(currentValue)
				currentValue = ''
				delimiter = 0

		finalHex = ''

		for each in range(len(finalArr)):
			getIndex = bin_val.index(finalArr[each])
			finalHex = finalHex + hex_val[getIndex]

		return finalHex

	'''
		Returns the xored value of the input string's binary
	'''
	def getFinalResult(self, newConvert):
		final = []
		for xd in range(len(self.xor)):
			final.append(self.xorGate(self.xor[xd], newConvert[xd]))
		final = ''.join(final)

		return final

	def increaseLen(self, xxd, leni):
		required = 128 - len(xxd)
		for sht in range(required):
			xxd.append(str(0))
		textLen = len(leni)
		textLenBin = str(format(textLen, 'b'))
		binLen = len(textLenBin)
		newConvert = []
		for nwCvrt in range(len(xxd)-binLen):
			newConvert.append(xxd[nwCvrt])
		for apdCvrt in range(binLen):
			newConvert.append(textLenBin[apdCvrt])
		
		return ''.join(newConvert)

	'''
		hash('string') - This takes in a string and hashes it
	'''
	def hash(self, input_i):
		self.firstBin = self.textBin(input_i)

		

		if len(self.firstBin) < 128:

			self.newConvert = self.increaseLen(self.firstBin, input_i)

		else:
			auths = {
				"counter": 0,
				"status": 0,
			}

			self.newConvert = []

			required = self.firstBin
			required = ''.join(required)
			
			while len(required) > 128:
				self.newConvert = []

				for appendo in range(len(required)):
					
					auths["counter"] = auths["counter"] + 1

					unitTest0 = auths["status"] == 0
					unitTest1 = auths["status"] == 1

					if auths["counter"] == 1:

						if unitTest0 == True:
							auths["status"] = 1
						elif unitTest1 == True:
							auths["status"] = 0

						auths["counter"] = 0

					if unitTest1 == True:
						self.newConvert.append(required[appendo])

				
				required = ''.join(self.newConvert)

			self.newConvert = ''.join(self.newConvert)

			if len(self.newConvert) < 128:
				self.newConvert = list(self.newConvert)
				self.newConvert = self.increaseLen(self.newConvert, input_i)

		
		self.xoredResult = self.getFinalResult(self.newConvert)
		self.finalHex = self.binToHex(self.xoredResult)

		return self.finalHex

