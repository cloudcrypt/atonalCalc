import pitchSet


class toneRow(pitchSet.pitchSet):
	debug = False
	isToneRow = False #won't need
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
	userSet = "" #need
	chordlist = []
	intlist = []
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
	hex1 = []
	hex2 = []
	
	def __init__(self, userString, debug=False):
		self.debug = debug
		self.userSet = userString
		self.process_set()
		self.rowList = self.intlist
		self.hex1 = self.intlist[:6]
		self.hex2 = self.intlist[6:]
		self.createMatrixList()
		self.adjIntSeries(intlist=self.rowList)