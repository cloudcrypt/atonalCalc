import fortenames
debug = False


class pitchSet:
	debug = False
	isToneRow = False
	note_int_mappings = {
		'c':0,
		'c+':1,
		'd-':1,
		'd':2,
		'd+':3,
		'e-':3,
		'e':4,
		'f':5,
		'f+':6,
		'g-':6,
		'g':7,
		'g+':8,
		'a-':8,
		'a':9,
		'a+':10,
		'b-':10,
		'b':11
	}
	userSet = ""      # from constructor
	chordlist = []    # from process_set
	intlist = []      # from process_set
	normalorder = []
	aisList = []
	aisString = ""
	primeList = []
	primeString = ""
	forteName = ""
	icvList = []
	icvString = ""
	ivList = []
	ivString = ""
	
	matrix = []
	rowList = []
	hexA = []
	hexB = []
	
	
	
	
	def __init__(self, userString, debug=False):
		self.debug = debug
		self.userSet = userString
		self.process_set()
		if not self.isToneRow:
			self.normalorder = self.convertNO(self.rotate())
			# need:
			(self.aisList, self.aisString) = self.adjIntSeries(self.normalorder)
			# instead of:
			#self.adjIntSeries()
			(self.primeList, self.primeString) = self.primeForm(self.normalorder, self.aisList)
			#self.primeForm()
			self.forteName = fortenames.getName(self.primeList)
			(self.icvList, self.icvString) = self.intervalClassVector(self.primeList)
			#self.intervalClassVector()
			(self.ivList, self.ivString) = self.indexVector(self.primeList)
			#self.indexVector()
			
			
		elif self.isToneRow:
			self.rowList = self.intlist
			self.hexA = self.intlist[:6]
			self.hexB = self.intlist[6:]
			self.createMatrixList()
			self.adjIntSeries(intlist=self.rowList)
		
	
	
	
	def process_set(self):
		if " " not in self.userSet:
			self.chordlist = [ note for note in self.userSet ]
		else:
			self.chordlist = [ note.lower() for note in self.userSet.split(' ') ]
		try:
			int(self.chordlist[0])
		except ValueError:
			for note in self.chordlist:
				self.intlist.append(self.note_int_mappings[note])
		else:
			templist = []
			for element in self.chordlist:
				if element.lower() == 't':
					templist.append(10)
				elif element.lower() == 'e':
					templist.append(11)
				else:
					templist.append(element)
			self.intlist = [ int(item) for item in templist ]
		if len(self.intlist) == 12:
			self.isToneRow = True
		return
		
	def rotate(self):
		if self.debug: print("***Intlist: %s***"%str(self.intlist))
		sorted_intlist = sorted(self.intlist)
		if self.debug: print("***Sorted Intlist: %s***"%str(sorted_intlist))
		n = 0
		list_of_intlists = []
		while n < len(sorted_intlist):
			list_of_intlists.append(sorted_intlist[n:] + sorted_intlist[:n])
			n += 1
		if self.debug: print("***Possible Rotations: %s***"%str(list_of_intlists))
		return list_of_intlists
	
	@staticmethod
	def staticRotate(intlist):
		if debug: print("***Intlist: %s***"%str(intlist))
		sorted_intlist = sorted(intlist)
		if debug: print("***Sorted Intlist: %s***"%str(sorted_intlist))
		n = 0
		list_of_intlists = []
		while n < len(sorted_intlist):
			list_of_intlists.append(sorted_intlist[n:] + sorted_intlist[:n])
			n += 1
		if debug: print("***Possible Rotations: %s***"%str(list_of_intlists))
		return list_of_intlists		

	@staticmethod	
	def convertNO(list_of_intlists):
		#rotations = set([ variant for variant in permutations(intlist) ])
		minim = 100
		smallest = []
		for variant in list_of_intlists:
			first = variant[0]
			last = variant[len(variant)-1]
			distance = (last - first) % 12
			#if last < first:
			#	distance = (12 - first) + last
			#else:
			#	distance = last - first
			if debug: print("***Min Dist Value: %d***"%minim)
			if debug: print("***Rotation: %s, Distance: %d***"%(str(variant),distance))
			if distance < minim:
				if debug: print("***Distance is less than min!***")
				minim = distance
				del smallest
				smallest = []
				smallest.append(variant)
				if debug: print("***Smallest: %s***"%str(smallest))
			elif distance == minim:
				if debug: print("***Distance is equal to min!***")
				if variant not in smallest:
					if debug: print("***Rotation was not in Smallest list***")
					smallest.append(variant)
					if debug: print("***Smallest: %s***"%str(smallest))
			else:
				if debug: print("***Distance is NOT less than min***")
		if len(smallest) > 1:
			if debug: print("***There are multiple smallest results!***")
			if debug: print("***Smallest: %s***"%str(smallest))
			# compare = {}
			# for option in smallest:
				# distance = (option[len(option)-2] - option[0]) % 12
				# compare[repr(option)] = distance
				# if debug: print("***Current Option: %s, Distance: %d***"%(str(option),distance))
			# if debug: print("***Comparison Results: %s***"%str(compare))
			n = -1
			while True:
				compare = pitchSet.detailCompare(smallest, n)
				if len(list(compare.values())) == len(set(list(compare.values()))):
					if debug: print("***There are NO distance duplicates!***")
					break
				else:
					if debug: print("***There are still distance duplicates!***")
				n -= 1
				if n == -(len(list_of_intlists[0])-1):
					if debug: print("***Last comparison detail index has been reached! Aborting detailCompare***")
					break		
			return eval(min(compare, key=compare.get))
		if debug: print("***There is only one result!***")
		return smallest[0]
	
	@staticmethod
	def detailCompare(list, n):
		if debug: print("***Detailed Comparison is Needed!***")
		if debug: print("***Index of comparison detail: %d***"%n)
		if debug: print("***Rotations to compare: %s***"%str(list))
		compare = {}
		for option in list:
			distance = (option[len(option)-1+n] - option[0]) % 12
			compare[repr(option)] = distance
			if debug: print("***Current Option: %s, Distance: %d***"%(str(option),distance))
		if debug: print("***Comparison Results: %s***"%str(compare))
		return compare		
	
	@staticmethod
	def adjIntSeries(intlist):
		#if intlist == None:
		#	intlist = self.normalorder
		n = 0
		result = []
		while n < len(intlist):
			try:
				if intlist[n+1] < intlist[n]:
					result.append((12 - intlist[n]) + intlist[n+1])
				else:
					result.append(intlist[n+1] - intlist[n])
				n += 1
			except IndexError:
				break
		index = 1
		resultstring = "<"
		for interval in result:
			if index == len(result):
				resultstring += str(interval)+">"
			else:
				resultstring += str(interval)+", "
			index += 1
		#if giveResult:
		#	return result
		#self.aisString = resultstring
		#self.aisList = result
		return (result, resultstring)
	
	@staticmethod
	def primeForm(normalorder, aisList):
		prime_list = [0]
		n = 0
		while True:
			if debug: print("***Left interval: %d***"%self.aisList[n])
			if debug: print("***Right interval: %d***"%self.aisList[len(self.aisList)-1-n])
			if aisList[n] < aisList[len(aisList)-1-n]:
				direction = "Normal"
				break
			elif aisList[n] > aisList[len(aisList)-1-n]:
				direction = "Reverse"
				break
			n += 1
			if n > len(aisList)-1-n:
				direction = "Normal"
				break
		# int(math.fabs(self.normalorder[1]-self.normalorder[0])) < int(math.fabs(self.normalorder[len(self.normalorder)-1]-self.normalorder[len(self.normalorder)-2]))	
		if direction == "Normal":
			if debug: print("//Normal prime reading//")
			n = 1
			while n < len(normalorder):
				prime_list.append(prime_list[n-1]+((normalorder[n]-normalorder[n-1])%12))
				n += 1
		elif direction == "Reverse":
			if debug: print("//Reverse prime reading//")
			n = len(normalorder)-1
			k = 0
			while n > 0:
				prime_list.append(prime_list[k]+((normalorder[n]-normalorder[n-1])%12))
				n -= 1
				k += 1
		result_string = "("
		for number in prime_list:
			result_string += str(number)
		result_string += ")"
		#self.primeString = result_string
		#self.primeList = prime_list
		return (prime_list, result_string)
		

	@staticmethod
	def intervalClassVector(primeList):
		if debug: print("***ICV Creation Start***")
		length = len(primeList)
		result = [0,0,0,0,0,0]
		occurrences = []
		n = 0
		while True:
			for number in primeList[(n+1):]:
				if debug: print("***Processing %d - %d ***"%(number,primeList[n]))
				occurrences.append(number - primeList[n])
			n += 1
			if n == len(primeList)-1:
				break
		if debug: print("***Occurrences: %s***"%str(occurrences))
		k = 1
		while k <= 6:
			for number in occurrences:
				if number == k or number == (12-k):
					result[k-1] += 1
			k += 1
		result_string = "["
		for number in result:
			result_string += str(number)
		result_string += "]"
		#self.icvString = result_string
		#self.icvList = result
		return (result, result_string)
			
	@staticmethod		
	def indexVector(primeList):
		if debug: print("***IV Creation Start***")
		occurrences = []
		result = [0,0,0,0,0,0,0,0,0,0,0,0]
		for number in primeList:
			for number2 in primeList:
				if debug: print("***Processing %d + %d ***"%(number,number2))
				if debug: print("***Result: %d***"%((number2+number)%12))
				occurrences.append((number2+number)%12)
		if debug: print("***Occurrences: %s***"%str(occurrences))
		for number in occurrences:
			result[number] += 1
		result_string = "<"
		for number in result:
			result_string += str(number)
		result_string += ">"
		#self.ivString = result_string
		#self.ivList = result
		return (result, result_string)
		
	def createMatrixList(self):
		matrix = []
		rowIndex = 0
		for transformation in self.rowList:
			matrix.append([])
			transformation = (12 - transformation)%12
			if transformation == 10:
				matrix[rowIndex].append("T")
			elif transformation == 11:
				matrix[rowIndex].append("E")
			else:
				matrix[rowIndex].append(transformation)
			for pitch in self.rowList[1:]:
				calculatedPitch = (pitch + transformation)%12
				if calculatedPitch == 10:
					matrix[rowIndex].append("T")
				elif calculatedPitch == 11:
					matrix[rowIndex].append("E")
				else:
					matrix[rowIndex].append(calculatedPitch)
			rowIndex += 1
		self.matrix = matrix
		return
		
		
		
		
		
		

	def display(self):
		print 'Notes:', self.chordlist
		print 'Integer form:', self.intlist
		if not self.isToneRow:
			print 'Normal order:', self.normalorder
			print 'Adjacent Interval Series:', self.aisString
			print 'Prime Form:', self.primeString
			print 'Forte Name:', self.forteName
			print 'Interval Class Vector:', self.icvString
			print 'Index Vector:', self.ivString
		elif self.isToneRow:
			print 'Matrix:'
			for row in self.matrix:
				print row
			print 'Row:', self.rowList
			print 'Adjacent Interval Series:', self.aisString
				
		
		
		
if __name__ == "__main__":
	inputString = raw_input("Please enter chord notes or numbers separated by spaces:")
	set = pitchSet(inputString)
	set.display()

