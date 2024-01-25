from flask import Flask, render_template, jsonify, request
from database import load_tours_from_db, load_tour_from_db, add_booking_to_db 

app = Flask(__name__)


@app.route("/")
def hello_world():
  tours_list = load_tours_from_db()
  return render_template("home.html",
                         tours=tours_list,
                         name="Lang Tengah Island")


@app.route("/api/tours")
def list_tour():
  tours_list = load_tours_from_db()
  return jsonify(tours_list)


@app.route("/tour/<id>")
def show_tour(id):
  tour = load_tour_from_db(id)
  if not tour:
    return "Not Found", 404
  return render_template("tourpage.html",
                         tour=tour,
                         name="Experience Lang Tengah")


@app.route("/tour/<id>/book", methods=["post"])
def book_tour(id):
  data = request.form
  name = load_tour_from_db(id)
  add_booking_to_db(id, data)
  return render_template("booking_submitted.html", 
                         booking=data, 
                         name=name)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
