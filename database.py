from sqlalchemy import create_engine, text 

db_connection_string = "mysql+pymysql://ptim3oy4g4rip1dmp7iv:pscale_pw_R26spDnwvnuwd8ozW5MI1nobfWWNFIgEJ1Op6BNz7Dx@aws.connect.psdb.cloud/langtengahisland?charset=utf8mb4"

engine = create_engine(db_connection_string, connect_args={
  "ssl": {
    "ssl_ca": "/etc/ssl/cert.pem"
    
  }
})


with engine.connect() as conn:
    result = conn.execute(text("select * from tours"))

    result_dicts = []
    for row in result.all():
        result_dicts.append(row._asdict())

    print(result_dicts)
