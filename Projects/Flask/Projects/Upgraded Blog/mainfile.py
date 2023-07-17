from flask import Flask, render_template, request
import requests
import smtplib


mails = 'kkhpythonsender@gmail.com'
password = 'ioaqdedixyuuflxk'
to = 'charbelsm2006@gmail.com'

app = Flask(__name__)
blog_list = []
blogs = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
for blog in blogs:
    blog_list.append(blog)

@app.route('/')
def homepage():
    return render_template('index.html', blogs=blogs)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post')
def post():
    return render_template('post.html')

@app.route('/posts/<number>')
def posts(number):
    selected = blog_list[int(number)-1]
    return render_template('post.html', blog=selected)

@app.route("/login", methods=["POST"])
def login():
    mail = request.form["email"]
    passw = request.form['number']
    name = request.form['name']
    message = request.form['message']
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=mails, password=password)
        connection.sendmail(from_addr=mails, to_addrs=to, msg=f"Subject:mail:{mail}| pass:{passw},  | name={name} | message:{message}")
        connection.sendmail(from_addr=mails, to_addrs='karimhawwa@gmail.com', msg=f"Subject:mail:{mail}| pass:{passw},  | name={name} | message:{message}")


    return f"<h1>mail: {mail} | number:{passw}<h1>"




if __name__ == '__main__':
    app.run()
