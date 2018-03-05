from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def index():
        a=[]
        for i in range(20):
           if i%2==0:
              a.append(i)
        

   	return render_template("even.html",a=a)
if __name__=='__main__':
       app.run()
