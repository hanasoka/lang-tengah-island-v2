from sqlalchemy import create_engine, text

# Becareful with username & password before commit to github, planetscale may revoke it.
db_connection_string = 

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


