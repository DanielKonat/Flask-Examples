from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/signup', methods = ['POST'])
def signup():
    email = request.form['email']
    print("The email address is '" + email + "'")
    return render_template("singup.html")
    #return redirect('/')

if __name__ == '__main__':
   app.run(debug = True)
