from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap4



class MyForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4)])
    submit = SubmitField("Submit")


app = Flask(__name__)

bootstrap = Bootstrap4(app)

app.secret_key = "balls"


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = MyForm()
    form.validate_on_submit()
    if form.validate_on_submit():
        print(form.email.data)
        print(form.password.data)
    if request.method == 'POST':
        if form.email.data.lower() == 'admin@ex' and form.password.data == 'admin':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
