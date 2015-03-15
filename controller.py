from pitchSet import *



def main():
	inputString = raw_input("Please enter chord notes or numbers separated by spaces:")
	set = pitchSet(inputString)
	if set.isToneRow:
		print "nope. this is a tone row"
	elif not set.isToneRow:
		set.display()
	
	
if __name__ == "__main__":
	main()