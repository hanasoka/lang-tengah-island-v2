from sqlalchemy import create_engine, text
import os

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

          



