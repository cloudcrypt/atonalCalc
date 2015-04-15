from pitchSet import *
from flask import jsonify

def transposeRow(integerString, row):
    transformation = getTransformation(integerString)
    result = []
    for pitch in row:
        calculatedPitch = (pitch + transformation ) % 12
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
        calculatedPitch = (((12 - pitch ) % 12) + transformation ) % 12
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
        calculatedPitch = (pitch + transformation ) % 12
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
        calculatedPitch = (((12 - pitch ) % 12) + transformation ) % 12
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
    print "transformer row:", row
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
    result_string_note1 = user_operation + ":"
    result_string_note2 = user_operation + ":"
    for element in result:
        if element == "T":
            elementForName = 10
        elif element == "E":
            elementForName = 11
        else:
            elementForName = element
        mapping1 = pitchSet.int_note_mappings_1[elementForName].upper()
        mapping2 = pitchSet.int_note_mappings_2[elementForName].upper()
        mapping1 = mapping1.replace('-', 'b')
        mapping1 = mapping1.replace('+', '#')
        mapping2 = mapping2.replace('-', 'b')
        mapping2 = mapping2.replace('+', '#')
        result_string += " " + str(element)
        result_string_note1 += " " + str(mapping1)
        result_string_note2 += " " + str(mapping2)
    finalResult = []
    finalResult.append(result_string)
    finalResult.append(result_string_note1)
    finalResult.append(result_string_note2)
    print finalResult
    return jsonify(list=finalResult)
	
	
	
                # mapping1 = self.int_note_mappings_1[pitchInt].upper()
                # mapping2 = self.int_note_mappings_2[pitchInt].upper()
                # mapping1 = mapping1.replace('-', 'b')
                # mapping1 = mapping1.replace('+', '#')
                # mapping2 = mapping2.replace('-', 'b')
                # mapping2 = mapping2.replace('+', '#')
                # self.matrixNote1[matrixPosition].append(mapping1)
                # self.matrixNote2[matrixPosition].append(mapping2)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
