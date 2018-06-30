from flask import Flask, render_template, request, url_for
import helpers as H

app= Flask("diceware")

@app.route("/simple")
def hello_world():
	# return "Hello World!"
	return render_template("simpleIndex.html")

@app.route("/")
def test():
	return render_template("index.html")

@app.route("/passwd")
def passwd():
	length=request.args.get("passwdLen")
	language= "en"
	try:
		if length == "": # or not isinstance(length, int):
			length=6
		else:
			length=int(length)
	except:
		length=6
	
	password= H.factory(app, length, language)

	# print (request.full_path)
	print (request.url)
	return (render_template("password.html",password=password))

if __name__ == "__main__":

	app.run(debug=True)