from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def base():
    return "Enter the Name"

@app.route('/<name>')
def info(name):
    Name = str(name)
    request_gender = requests.get(f"https://api.genderize.io?name={name}")
    gender_data = request_gender.json()
    gender = gender_data['gender']

    request_age = requests.get(f"https://api.agify.io?name={name}")
    age_data = request_age.json()
    age = age_data['age']
    return render_template('guess.html', gender=gender, person_name=Name, age=age)

if __name__ =='__main__':
    app.run(debug=True)