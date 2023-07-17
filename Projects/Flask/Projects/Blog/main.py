from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    blogs_data = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    blogs = blogs_data.json()
    print(blogs)
    return render_template("main.html", blogs=blogs)

@app.route('/blog/<number>')
def get_blog(number):
    requested = None
    bloged = requests.get('https://api.npoint.io/c790b4d5cab58020d391').json()
    for post in bloged:
        print(post['id'])
        if int(post['id']) == int(number):
            requested = post
    return render_template('post.html',  post=requested)

if __name__ == "__main__":
    app.run(debug=True)
