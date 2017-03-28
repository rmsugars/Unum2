class unumSys:
#	exacts = {}
	def __init__(self, lattice):
		self.lattice = lattice
		self.generateExacts()

	def generateExacts(self):
		latLen = len(self.lattice)
		exacts = {}
		for i,num in enumerate(self.lattice):
			exacts[latLen-i] =1/num
			exacts[latLen+i] = num
			exacts[3*latLen-i] = -num
			exacts[3*latLen+i] = -1/num
		exacts[0] = 0
		exacts[2*latLen] = float('inf')
		self.exacts = sorted(exacts.items())

	def outputExacts(self):
		tries = self.exacts[-1][0]+1
		numbits = (tries+1).bit_length()
		for i in range(tries):
			try:
				temp = self.exacts[i][1]
			except:
				temp = "none"
			print("{0:0={1}b} => {2}".format(i<<1,numbits,temp))

	def numToUnum(self,num):
		isExact = False
		latLen = len(self.lattice)
		prevDiff = 2 * self.lattice[-1]
		for i in self.exacts:
			if (i[1] <= num):
				diff = num - i[1]
				if diff < prevDiff:
					prevDiff = diff
					value = self.exacts[i[0]][0]
		ans = value << 1
		if prevDiff != 0:
			ans = ans+1
		return ans

	def genAddLut(self):
		addLut = {}
		for i in exacts:
			addLut[i<<1] = {}
			for j in exacts:
				addLut[i<<1][j<<1] = 5 #change this 
