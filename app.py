from flask import Flask, render_template, request, url_for, make_response, session, redirect, g, flash
from pitchSet import *
#import psycopg2, sqlite3, bcrypt
#from random import randint

#DATABASE = 'postgres://wzixescuopzqdc:r3zTn8Hsuso1rfdzdX1mQ2M2ty@ec2-54-235-193-41.compute-1.amazonaws.com:5432/de5augokmm67pb'
app = Flask(__name__)
#app.config.from_object(__name__)
# ######## need to regenerate! app.secret_key = '\x80\x0e.\x97\xd4\xc0\x8a\xef@\xf4O\xd6w\x04V\x04[\xdf\x01dP\x9b\x07\x17'




@app.route("/")
def index():
	return render_template("home.html")

@app.route("/analyse", methods=['GET'])
def analyse():
	set = request.args.get('set')
	if isToneRow(set):
		return set + " implementation of tone row analysis in progress"
	
	analysedSet = pitchSet(set)
	return render_template("set.html", set=analysedSet)
	
def isToneRow(set):
	intlist = []
	if " " not in set:
		chordlist = [ note for note in set ]
	else:
		chordlist = [ note.lower() for note in set.split(' ') ]
	try:
		int(chordlist[0])
	except ValueError:
		for note in chordlist:
			intlist.append(pitchSet.note_int_mappings[note])
	else:
		templist = []
		for element in chordlist:
			if element.lower() == 't':
				templist.append(10)
			elif element.lower() == 'e':
				templist.append(11)
			else:
				templist.append(element)
		intlist = [ int(item) for item in templist ]
	if len(intlist) == 12:
		return True
	else:
		return False

if __name__ == '__main__':
    app.run(debug=True)
	
	
	