from flask import Flask, render_template, request, url_for, make_response, session, redirect, g, flash
import transformer
from pitchSet import *
from toneRow import *
#import psycopg2, sqlite3, bcrypt
#from random import randint

#DATABASE = 'postgres://wzixescuopzqdc:r3zTn8Hsuso1rfdzdX1mQ2M2ty@ec2-54-235-193-41.compute-1.amazonaws.com:5432/de5augokmm67pb'
app = Flask(__name__)
#app.config.from_object(__name__)
app.secret_key = '\xdc\xae\xd5\xce\x9a\x83\x8d\xe1\x0e\xe7K>\xc5O\x18\xa0\r6\x87=\xf8\xe3<\x88'




@app.route("/")
def index():
	return render_template("home.html")

@app.route("/analyse", methods=['GET'])
def analyse():
	set = request.args.get('set')
	if isToneRow(str(set)):
		analysedSet = toneRow(set)
		if 'current_set' in session: session.pop('current_set')
		session['current_set'] = analysedSet.rowList
		return render_template("row.html", row=analysedSet)
	
	analysedSet = pitchSet(set)
	if 'current_set' in session: session.pop('current_set')
	session['current_set'] = analysedSet.intlist
	return render_template("set.html", set=analysedSet)
	
@app.route("/transform", methods=['GET'])
def transform():
	userTransformation = request.args.get('transformation')
	return transformer.performOperation(userTransformation, session['current_set'])
	
@app.route('/session')
def viewSession():
    data = {}
    for item in session:
        data[item] = session[item]
    #return jsonify(**data)
    return str(data)
	
@app.route('/sessionclear')
def clearSession():
    sessionData = []
    for item in session:
        sessionData.append(item)
    for item in sessionData:
        session.pop(item)
    return "// Session has been cleared //"
	
	
	
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
	
	
	