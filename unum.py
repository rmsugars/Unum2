#classes for unum2.0
#created by reuben sugars 2017

class unum:
	#ulattice length is 2**(bitSize-3)
	maxIndex = 0
	nums = []
	def __init__(self,ulattice):
		self.ulattice = ulattice
		self.bitSize = len(ulattice) + 1 #log2(len(ulattice))+3
		self.maxIndex = 2**self.bitSize
		unum.genNums(self)

	def genNums(self):
		notInfinity = float('nan') #this needs to be changed
		self.nums = []
		loopsize = (self.bitSize-3 << 1) -1
		self.addNum('intervalLow',0)
		for i in range(loopsize):
			self.addNum('intervallow',1/self.ulattice[-(i+1)])
		self.addNum('intervalhigh',1)
		for i in range(loopsize):
			self.addNum('intervalhigh',self.ulattice[i+1])
		self.addNum('negIntervalHigh',notInfinity)
		for i in range(loopsize):
			self.addNum('negintervalhigh',-self.ulattice[-(i+1)])
		self.addNum('negintervallow',-1)
		for i in range(loopsize):
			self.addNum('negintervallow',-1/self.ulattice[i+1])

	def genAddLut(self):
		self.addLut = {}
		rangeMax = len(self.nums)
		for i in range(0,rangeMax,2):
			self.addLut[i] = {}
			for j in range(0,rangeMax,2):
				ans = self.nums[i] + self.nums[j]
				if (ans in self.nums):
					try:
						self.addLut[i][j]=self.nums.index(ans)
					except e:
						print("error\n")
	def addNum(self, name, value):
		self.nums.append(value)
		self.nums.append(name)

	def printNums(self):
		for i in range(len(self.nums)):
			print(bin(i), " = ", self.nums[i])
