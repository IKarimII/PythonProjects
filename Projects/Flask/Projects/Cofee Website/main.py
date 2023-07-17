from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, IntegerField, SelectField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    url = URLField('Location Link', validators=[DataRequired()])
    opentime = IntegerField("opening time",validators=[DataRequired()])
    closetime = IntegerField("closing time", validators=[DataRequired()])
    wifi = SelectField("Wifi Rating", validators=[DataRequired()], choices=[('💪'), ('💪💪'), ('💪💪💪'), ('💪💪💪💪'), ( '💪💪💪💪💪')])
    coffee = SelectField("Cofee", validators=[DataRequired()], choices=[('☕️'), ('☕️☕️'), ('☕️☕️☕️'), ('☕️☕️☕️☕️'), ( '☕️☕️☕️☕️☕️')])
    power = SelectField("Power", validators=[DataRequired()], choices=[('🔌'), ('🔌🔌'), ('🔌🔌🔌️'), ('🔌🔌🔌🔌'), ( '🔌🔌🔌🔌🔌')])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["POST", "GET"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")

    if form.validate_on_submit():
        with open('cafe-data.csv', 'a', encoding='utf-8') as file:
            file.write(f'\n{form.cafe.data},{form.url.data},{form.opentime.data},{form.closetime.data},{form.wifi.data},{form.coffee.data},{form.power.data}')
        return render_template('cafes.html')

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
