from flask import Flask,render_template
app=Flask(__name__)

@app.route('/y')
def hello():
          color=['orange','red','Black','Green']  
          return render_template('dropcolor.html',color=color)

if __name__=='__main__':
	app.run(debug=True)
