import os

from sqlalchemy import create_engine, text

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string, connect_args={
  "ssl": {
    "ssl_ca": "/etc/ssl/cert.pem"
    
  }
})

def load_tours_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from tours"))
    tours = []
    for row in result.all():
        tours.append(row._asdict())
    return tours

def load_tour_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from tours where id = :val"), {"val": id})
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      #return dict(rows[0])
      return rows[0]._asdict()


def add_booking_to_db(tour_id, booking):
  with engine.connect() as conn:
    query = text("INSERT INTO booking_request(tour_id, full_name, phone, email, travel_date, adult, child, toddler) "
                       "VALUES(:tour_id, :full_name, :phone, :email, :travel_date, :adult, :child, :toddler)")

    conn.execute(query, 
                       {"tour_id": tour_id,
                        "full_name": booking['full_name'],
                        "phone": booking['phone'],
                        "email": booking['email'],
                        "travel_date": booking['travel_date'],
                        "adult": booking['adult'],
                        "child": booking['child'],
                        "toddler": booking['toddler']})

    
   



