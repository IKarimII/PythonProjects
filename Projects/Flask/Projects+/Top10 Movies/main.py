from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

db = SQLAlchemy()

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Movies.db"
# initialize the app with the extension
db.init_app(app)


class MyForm(FlaskForm):

    review = StringField('Review', validators=[DataRequired()])
    rating = IntegerField("Rating", validators=[DataRequired()])
    submit = SubmitField('Change Review')


class Add(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    submit = SubmitField('Add')


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    year = db.Column(db.String(250))
    description = db.Column(db.String)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String)
    img_url = db.Column(db.String)


with app.app_context():
    db.create_all()

# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# second_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )
# with app.app_context():
#     db.session.add(new_movie)
#     db.session.add(second_movie)
#     db.session.commit()


@app.route('/')
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_books = result.scalars()
    return render_template('index.html', movies=all_books)

@app.route('/add', methods=["POST","GET"])
def add():
    form = Add()

    if request.method == 'POST':
        response = requests.get('https://api.themoviedb.org/3/search/movie', params={"api_key": '1b8d56d107225d896f0b15e4dd9f8041', "query": form.title.data})
        data = response.json()["results"]
        print(data)
        return render_template('select.html', data=data)

    return render_template('add.html', form=form)


@app.route('/select/<ids>', methods=["POST", "GET"])
def select(ids):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{ids}',
                            params={"api_key": '1b8d56d107225d896f0b15e4dd9f8041'})

    data = response.json()
    print(data)
    with app.app_context():
        new_book = Movie(
            title=data['title'],
            description=data['overview'],
            year=data['release_date'],
            img_url=f"http://image.tmdb.org/t/p/w500{data['poster_path']}",
            rating=-data['popularity'],
            ranking=0,
            review="gd",
        )
        db.session.add(new_book)
        db.session.commit()
    return redirect(url_for('home'))



@app.route('/edit/<ids>', methods=["POST", "GET"])
def edit(ids):
    form = MyForm()
    if request.method == 'POST':
        with app.app_context():
            book_to_update = db.session.execute(db.select(Movie).where(Movie.id == ids)).scalar()
            book_to_update.review = form.review.data
            book_to_update.rating = form.rating.data
            db.session.commit()
        return redirect(url_for('home'))
    book_selected = db.get_or_404(Movie, ids)
    return render_template("edit.html", movie=book_selected, form=form)


@app.route("/delete/<ids>", methods=["POST", "GET"])
def delete(ids):
    with app.app_context():
        book_to_delete = db.session.execute(db.select(Movie).where(Movie.id == ids)).scalar()
        db.session.delete(book_to_delete)
        db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
