from sqlalchemy import create_engine, text 

db_connection_string = "mysql+pymysql://y3n7542zq0m9weeptp74:pscale_pw_pzIxQwS7Li8pAlBln7krxjpK5LqqANA1qdlYDKt8Hnx@aws.connect.psdb.cloud/langtengahisland?charset=utf8mb4"

engine = create_engine(db_connection_string, connect_args={
  "ssl": {
    "ssl_ca": "/etc/ssl/cert.pem"
    
  }
})


with engine.connect() as conn:
    result = conn.execute(text("select * from tours"))
    print("type(result):", type(result))
    
    result_all = result.all()
    print("type(result_all):", type(result_all))
    print("result_all():", result_all)
  
    first_result = result_all[0]
    print("type(first_result):", type(first_result))
    print("first_result:", first_result)
  
    first_result_dict = first_result._asdict()
    print("type(first_result_dict):", type(first_result_dict))
    print("first_result_dict:", first_result_dict)
    
