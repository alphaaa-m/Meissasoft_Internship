from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

username = "root"
password = "M%40them%40tics3"
host = "127.0.0.1"
port = 3306
database_name = "py_database"

DATABASE_URL = f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database_name}"

engine = create_engine(DATABASE_URL)

LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
