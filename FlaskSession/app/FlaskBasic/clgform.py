from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def homepage():

   	return render_template("whome.html")

@app.route('/aboutus')
def aboutpage():

   	return render_template("aboutus.html")

@app.route('/reg')
def conpage():

   	return render_template("reg.html")


if __name__=="__main__":
	app.run(host='0.0.0.0',port=5000)
