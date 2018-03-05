from flask import Flask,render_template
app=Flask(__name__)

@app.route('/yo')
def hello():
       # sub=[{'subject':'Maths',
        #      'Marks':80},
	 #    {'subject':'C',
	#	'Marks':70},
	 #    {'subject':'java',
	  #    'Marks':60}]
           sub={'maths':'80','c':'70','java':'60'}    
           return render_template('table.html',a=sub)
#hello(name)
if __name__=='__main__':
	app.run(debug=True)
