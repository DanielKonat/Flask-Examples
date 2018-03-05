from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      a=request.form['name']
      b=request.form['city']
      print("The email address is '" + email + "'")
      return "Name : "+request.method+"  "+a+"    "+b
   else:
      return "error"
if __name__ == '__main__':
   app.run(debug = True)
