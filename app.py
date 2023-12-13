from flask import Flask, render_template

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


@app.route("/")
def hello_world():
    return render_template("home.html", tours=TOURS, name="Lang Tengah Island")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)  