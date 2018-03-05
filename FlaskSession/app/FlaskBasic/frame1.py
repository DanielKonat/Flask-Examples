from flask import Flask,render_template
app=Flask(__name__)
@app.route('/hello/<user>')

def hello_name(user):
      p1="here is an intresting quote for you"
      p2="the limits of my language are the limits of my mind.all know is what i have word for u "
      return render_template('hello.html',name=user,para1=p1,para2 =p2)

if __name__=='__main__':
    app.run(debug=True)

