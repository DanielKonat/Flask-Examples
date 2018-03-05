from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField,RadioField,SelectField

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class RegistrationForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    rollno=TextField('Rollno:',validators=[validators.required(),validators.Length(min=0, max=4)])
    Class=TextField('Class:', validators=[validators.required()])
    gender=RadioField('Gender:', validators=[validators.required()])
    address=TextField('Address:', validators=[validators.required()])
    bloodgroup=SelectField('BloodGroup:', validators=[validators.required()])
    email = TextField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
@app.route('/',methods=['GET','POST'])
def hiii():
    form=RegistrationForm(request.form)
    print form.errors
    if request.method == 'POST':
        name=request.form['name']
        rollno=request.form['rollno']
        Class=request.form['class']
        gender=request.form['gender']
        address=request.form['address']
        bloodgroup=request.form['bloodgroup']        
        email=request.form['email']
        print name, " ", rollno, " ",Class , " ",gender, " ",address, " ",bloodgroup, " ",email

        
        if form.validate():
            # Save the comment here.
            flash('Thanks for registration ' + name)
        else:
            flash('Error: All the form fields are required. ')
 
    return render_template('hell.html', form=form)
 
if __name__ == "__main__":
    app.run()
  
