from flask import Flask, render_template, jsonify 
from database import engine

app = Flask(__name__)

TOURS = [
  {
    "id": 1,
    "title": "Day Trip",
    "description": "A day trip to Lang Tengah Island",
    "price": "MYR 500.00"
  },

  {
    "id": 2,
    "title": "Family Picnic",
    "description": "A beach picnic at Turtle Bay",
    "price": "MYR 1,000.00"
  },

  {
    "id": 3,
    "title": "Group Trip",
    "description": "Explore Lang Tengah Island",
    "price": "MYR 5,000.00"
  },

  {
    "id": 4,
    "title": "Private Trip",
    "description": "Picnic, Adventure, Exploration",

  }
]

def load_tours_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from tours"))
    result_dicts = []
    for row in result.all():
        result_dicts.append(row._asdict())

@app.route("/")
def hello_world():
    return render_template("home.html", tours=TOURS, name="Lang Tengah Island")

@app.route("/api/tours")
def list_tour():
    return jsonify(TOURS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)  