from backend.db.models.model_user import Base
from backend.db.session_maker import engine


def create_tables():
    Base.metadata.create_all(bind=engine)


def drop_tables():
    Base.metadata.drop_all(bind=engine)


def drop_create():
    drop_tables()
    create_tables()

