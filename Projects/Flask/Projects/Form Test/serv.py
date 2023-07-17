from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def Homepage():
    return render_template('homepage.html')

@app.route("/login", methods=["POST"])
def login():
    mail = request.form["email"]
    passw = request.form['password']
    return f"<h1>mail: {mail} \n pass:{passw}<h1>"


if __name__ =='__main__':
    app.run()