from flask import Flask,render_template
app=Flask(__name__)
@app.route('/hello/')

def hello_name():
    lista=['dhiraj','amar','danny','yash']
    for a in len(lista):
      lt=lista[a]
      return render_template('diclistuple.html',li=lt)

if __name__=='__main__':
     app.run(debug=True)

