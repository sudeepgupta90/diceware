from ast import literal_eval
from random import randint

def generatePasswd(n):

	li=[]
	for _ in range(n):
		x=[]
		for _ in range(5):
			x.append(str(randint(1,6)))

		x= "".join(x)
		li.append(x)

	return li

def translatePasswd(app,li, language):
	resource= language+"_words.txt"
	f= app.open_resource("static/"+resource, "r")
	passwd_list=literal_eval(f.read())
	f.close()

	passwd= ""
	for x in li:
		passwd+= passwd_list[x]+" "

	return passwd

def factory(app, length=6, language="en"):
	li= generatePasswd(length)
	passwd= translatePasswd(app, li, language)

	return passwd
