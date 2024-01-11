from sqlalchemy import create_engine, text 

engine = create_engine("mysql+pymysql://tht1jzixhqku3wu1ov9s:pscale_pw_MGwkWDFzm2bTVTqymhrxz05BBPsmWfFwdAfzVfWOa5I@aws.connect.psdb.cloud/langtengahisland?charset=utf8mb4")


with engine.connect() as conn:
    result = conn.execute(text("select * from tours"))
    print(result.all())
