from pitchSet import *


class toneRow(pitchSet):
    debug = False

    matrix = []
    matrixNote1 = []
    matrixNote2 = []
    rowList = []

    hexA = []
    hexAICVString = ""
    hexAIVString = ""

    hexB = []
    hexBICVString = ""
    hexBIVString = ""

    rowAISList = []
    rowAISString = ""

    subTriChord1 = []
    subTriChord1PrimeString = ""
    subTriChord2 = []
    subTriChord2PrimeString = ""
    subTriChord3 = []
    subTriChord3PrimeString = ""
    subTriChord4 = []
    subTriChord4PrimeString = ""

    subTetraChord1 = []
    subTetraChord1PrimeString = ""
    subTetraChord2 = []
    subTetraChord2PrimeString = ""
    subTetraChord3 = []
    subTetraChord3PrimeString = ""

    triDerived = False
    tetraDerived = False

    isSymmetrical = False

    isAllInterval = True

    def __init__(self, userString, debug=False):

        self.debug = debug
        self.userSet = userString
        self.process_set()
        self.rowList = self.intlist
        self.hexA = self.intlist[:6]
        self.hexB = self.intlist[6:]
        self.createMatrixList()
        (self.rowAISList, self.rowAISString) = self.adjIntSeries(self.rowList)

        self.hexAICVString = self.intervalClassVector(self.toPrimeForm(self.hexA)[0])[1]
        self.hexBICVString = self.intervalClassVector(self.toPrimeForm(self.hexB)[0])[1]

        self.hexAIVString = self.indexVector(self.hexA)[1]
        self.hexBIVString = self.indexVector(self.hexB)[1]

        self.subTriChord1 = self.rowList[:3]
        self.subTriChord1PrimeString = self.toPrimeForm(self.subTriChord1)[1]
        self.subTriChord2 = self.rowList[3:6]
        self.subTriChord2PrimeString = self.toPrimeForm(self.subTriChord2)[1]
        self.subTriChord3 = self.rowList[6:9]
        self.subTriChord3PrimeString = self.toPrimeForm(self.subTriChord3)[1]
        self.subTriChord4 = self.rowList[9:12]
        self.subTriChord4PrimeString = self.toPrimeForm(self.subTriChord4)[1]

        self.subTetraChord1 = self.rowList[:4]
        self.subTetraChord1PrimeString = self.toPrimeForm(self.subTetraChord1)[1]
        self.subTetraChord2 = self.rowList[4:8]
        self.subTetraChord2PrimeString = self.toPrimeForm(self.subTetraChord2)[1]
        self.subTetraChord3 = self.rowList[8:12]
        self.subTetraChord3PrimeString = self.toPrimeForm(self.subTetraChord3)[1]

        if self.subTriChord1PrimeString == self.subTriChord2PrimeString and self.subTriChord1PrimeString == self.subTriChord3PrimeString and self.subTriChord1PrimeString == self.subTriChord4PrimeString:
            self.triDerived = True
        if self.subTetraChord1PrimeString == self.subTetraChord2PrimeString and self.subTetraChord1PrimeString == self.subTetraChord3PrimeString:
            self.tetraDerived = True

        if self.rowAISList == self.rowAISList[::-1]:
            self.isSymmetrical = True
        elif self.subTetraChord1PrimeString == self.subTetraChord3PrimeString:
            self.isSymmetrical = True
        elif self.subTriChord1PrimeString == self.subTriChord4PrimeString and self.subTriChord2PrimeString == self.subTriChord3PrimeString:
            self.isSymmetrical = True

        for number in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
            if number not in self.rowAISList:
                self.isAllInterval = False


    @staticmethod
    def toPrimeForm(intlist):
        intlistNO = pitchSet.convertNO(pitchSet.staticRotate(intlist))
        return pitchSet.primeForm(intlistNO, pitchSet.adjIntSeries(intlistNO)[0])

    def createMatrixList(self):
        matrix = []
        rowIndex = 0
        for transformation in self.rowList:
            matrix.append([])
            transformation = (12 - transformation) % 12
            if transformation == 10:
                matrix[rowIndex].append("T")
            elif transformation == 11:
                matrix[rowIndex].append("E")
            else:
                matrix[rowIndex].append(transformation)
            for pitch in self.rowList[1:]:
                calculatedPitch = (pitch + transformation) % 12
                if calculatedPitch == 10:
                    matrix[rowIndex].append("T")
                elif calculatedPitch == 11:
                    matrix[rowIndex].append("E")
                else:
                    matrix[rowIndex].append(calculatedPitch)
            rowIndex += 1
        self.matrix = matrix
        #self.matrixNote1 = matrix
        #self.matrixNote2 = matrix
        matrixPosition = 0
        for row in self.matrix:
            rowPosition = 0
            self.matrixNote1.append([])
            self.matrixNote2.append([])
            for pitch in row:
                if pitch == 'T':
                    pitchInt = 10
                elif pitch == 'E':
                    pitchInt = 11
                else:
                    pitchInt = matrix[matrixPosition][rowPosition]
                mapping1 = self.int_note_mappings_1[pitchInt].upper()
                mapping2 = self.int_note_mappings_2[pitchInt].upper()
                mapping1 = mapping1.replace('-', 'b')
                mapping1 = mapping1.replace('+', '#')
                mapping2 = mapping2.replace('-', 'b')
                mapping2 = mapping2.replace('+', '#')
                self.matrixNote1[matrixPosition].append(mapping1)
                self.matrixNote2[matrixPosition].append(mapping2)
                rowPosition += 1
            matrixPosition += 1
        return

    def display(self):
        print 'Notes:', self.chordlist
        print 'Integer form:', self.intlist
        print 'Matrix:'
        for row in self.matrix:
            print row
        print 'Row:', self.rowList
        print 'Adjacent Interval Series:', self.rowAISString
        print self.subTetraChord1
        print self.subTetraChord1PrimeString
        print self.subTetraChord2
        print self.subTetraChord2PrimeString
        print self.subTetraChord3
        print self.subTetraChord3PrimeString


if __name__ == "__main__":
    inputString = raw_input("Please enter chord notes or numbers separated by spaces:")
    set = toneRow(inputString)
    set.display()
    print set.__dict__
    print set.isAllInterval
    print set.isSymmetrical
    print set.triDerived
    print set.tetraDerived