from sqlalchemy import create_engine
url = "mysql+pymysql://root:M%40them%40tics3@127.0.0.1:3306/py_database"


try:
    engine = create_engine(url)
    conn = engine.connect()
    print("✅ Connected to MySQL!")
except Exception as e:
    print("❌ Failed to connect:", e)