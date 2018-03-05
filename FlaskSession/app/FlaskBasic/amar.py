from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def homepage():

   	return render_template("form.html")
@app.route('/result1',methods = ['POST', 'GET'])
def result1():
   if request.method == 'POST':
      result1 = request.form
      print result1
      return render_template("result1.html",result1 = result1)


if __name__=="__main__":
	app.run(host='0.0.0.0',port=5000)
