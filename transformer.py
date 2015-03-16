

def transposeRow(integerString, row):
	transformation = getTransformation(integerString)
	result = []
	for pitch in row:
		calculatedPitch = (pitch + transformation)%12
		if calculatedPitch == 10:
			result.append('T')
		elif calculatedPitch == 11:
			result.append('E')
		else:
			result.append(calculatedPitch)
	return result
	
def invertRow(integerString, row):
	transformation = getTransformation(integerString)
	result = []
	for pitch in row:
		calculatedPitch = (((12 - pitch)%12) + transformation)%12
		if calculatedPitch == 10:
			result.append('T')
		elif calculatedPitch == 11:
			result.append('E')
		else:
			result.append(calculatedPitch)
	return result	
	
def retrogradeRow(integerString, row):
	transformation = getTransformation(integerString)
	result = []
	for pitch in row:
		calculatedPitch = (pitch + transformation)%12
		if calculatedPitch == 10:
			result.append('T')
		elif calculatedPitch == 11:
			result.append('E')
		else:
			result.append(calculatedPitch)
	result.reverse()
	return result

def retrogradeInvertRow(integerString, row):
	transformation = getTransformation(integerString)
	result = []
	for pitch in row:
		calculatedPitch = (((12 - pitch)%12) + transformation)%12
		if calculatedPitch == 10:
			result.append('T')
		elif calculatedPitch == 11:
			result.append('E')
		else:
			result.append(calculatedPitch)
	result.reverse()
	return result
	
def getTransformation(integerString):
	if integerString == "T":
		transformation = 10
	elif integerString == "E":
		transformation = 11
	else:
		transformation = int(integerString)
	return transformation
	
	
def performOperation(user_operation, row):
	user_operation = user_operation.upper()
	if user_operation[0:1] == "P":
		result = transposeRow(user_operation[1:], row)
	elif user_operation[0:1] == "I":
		result = invertRow(user_operation[1:], row)
	elif user_operation[0:1] == "R" and user_operation[0:2] != "RI":
		result = retrogradeRow(user_operation[1:], row)
	elif user_operation[0:2] == "RI":
		result = retrogradeInvertRow(user_operation[2:], row)
	result_string = user_operation + ":"
	for element in result:
		result_string += " " + str(element)
	return result_string
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
