from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from db_config import db_url, local_db_url


engine = create_engine(db_url, echo=True)
Session = sessionmaker(bind=engine)
drop_create_engine = create_engine(local_db_url, echo=True)