from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, IntegerField, SelectField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy


class MyForm(FlaskForm):
    name = StringField('Book Name', validators=[DataRequired()])
    author = StringField('Book Author', validators=[DataRequired()])
    rating = IntegerField("Rating", validators=[DataRequired()])
    submit = SubmitField('ADD BOOK')


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap = Bootstrap5(app)

# create the extension
db = SQLAlchemy()

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
# initialize the app with the extension
db.init_app(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()

@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    form = MyForm()
    if request.method == 'POST':
        with app.app_context():
            new_book = Book(
                title=form.name.data,
                author=form.author.data,
                rating=form.rating.data
            )
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=form)


@app.route("/delete/<ids>", methods=["POST", "GET"])
def delete(ids):
    with app.app_context():
        book_to_delete = db.session.execute(db.select(Book).where(Book.id == ids)).scalar()
        db.session.delete(book_to_delete)
        db.session.commit()
    return redirect(url_for('home'))


@app.route("/edit/<ids>", methods=["POST", "GET"])
def edit(ids):
    form = MyForm()
    if request.method == 'POST':
        with app.app_context():
            book_to_update = db.session.execute(db.select(Book).where(Book.id == ids)).scalar()
            book_to_update.title = form.name.data
            book_to_update.author = form.author.data
            book_to_update.rating = form.rating.data
            db.session.commit()
        return redirect(url_for('home'))
    book_selected = db.get_or_404(Book, ids)
    return render_template("edit.html", book=book_selected, form=form)


if __name__ == "__main__":
    app.run(debug=True)
