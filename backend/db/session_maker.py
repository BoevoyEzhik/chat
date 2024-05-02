from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from backend.db.db_config import db_url


engine = create_engine(db_url, echo=True)
Session = sessionmaker(bind=engine)
