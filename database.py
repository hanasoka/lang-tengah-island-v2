from sqlalchemy import create_engine, text 

# Becareful with username & password before commit to github, planetscale may revoke it.
db_connection_string = 

engine = create_engine(db_connection_string, connect_args={
  "ssl": {
    "ssl_ca": "/etc/ssl/cert.pem"
    
  }
})



