class unumSys:
	exacts = {}
	def __init__(self, lattice):
		self.lattice = lattice
		self.generateNums()

	def generateNums(self):
		latLen = len(self.lattice)
		for i,num in enumerate(self.lattice):
			self.exacts[latLen-i] =1/num
			self.exacts[latLen+i] = num
			self.exacts[3*latLen-i] = -num
			self.exacts[3*latLen+i] = -1/num

	def outputExacts(self):
		tries = max(self.exacts)+1
		numbits = 7
		for i in range(tries):
			try:
				temp = self.exacts[i]
			except:
				temp = "none"
			print("{0:0={1}b} => {2}".format(i,numbits,temp))
