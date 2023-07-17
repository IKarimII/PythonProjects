from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
API_KEY = "GAY"

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500))
    img_url = db.Column(db.String(500))
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250))
    has_toilet = db.Column(db.String)
    has_wifi = db.Column(db.String)
    has_sockets = db.Column(db.String)
    can_take_calls = db.Column(db.String)
    coffee_price = db.Column(db.String(250))

    def to_dict(self):
        # Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary

        # Method 2. Altenatively use Dictionary Comprehension to do the same thing.
        # return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route("/random")
def random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def all_cafe():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes])


@app.route("/search")
def search_cafe():
    query_location = request.args.get("loc")
    cafe = db.session.query(Cafe).filter_by(location=query_location).first()
    if cafe:
        return jsonify(cafe=cafe.to_dict())
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    cafe = Cafe(
        name=request.args.get("name"),
        map_url=request.args.get("map_url"),
        img_url=request.args.get("img_url"),
        location=request.args.get("loc"),
        seats=request.args.get("seats"),
        has_toilet=request.args.get("has_toilet"),
        has_wifi=request.args.get("has_wifi"),
        has_sockets=request.args.get("has_sockets"),
        can_take_calls=request.args.get("can_take_calls"),
        coffee_price=request.args.get("coffee_price"),
    )
    db.session.add(cafe)
    db.session.commit()
    return jsonify(success={"Added": "The Cafe was Added"})


## HTTP PUT/PATCH - Update Record
@app.route("/patch/<ids>", methods=["POST", "GET", "PATCH"])
def patch_cafe(ids):
    cafe_to_patch = db.session.query(Cafe).get(ids)
    new_price = request.args.get("new_price")
    if cafe_to_patch:
        cafe_to_patch.coffee_price = new_price
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})


## HTTP DELETE - Delete Record
@app.route("/delete/<ids>", methods=["Delete"])
def delete_cafe(ids):
    cafe_to_delete = db.session.query(Cafe).get(ids)
    if cafe_to_delete:
         if request.args.get("API_KEY") == API_KEY:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(response={"success": "Successfully Deleted the cafe."})
         else:

             return jsonify(error={"REJECTED": "Wrong API KEY"})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})



if __name__ == '__main__':
    app.run(debug=True)
