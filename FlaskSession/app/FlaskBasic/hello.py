from flask import Flask,render_template
app=Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
	#return render_template("abc.html",name=name)
        return("hello %s" % name)

@app.route('/hello/<float:name>')
def hello1(name):

	#return render_template("abc.html",name=name)
        return("hello %s" % name)

if __name__=='__main__':
	app.run(debug=True)
