from models.model_user import Base
from session_maker import drop_create_engine


def create_tables():
    Base.metadata.create_all(bind=drop_create_engine)


def drop_tables():
    Base.metadata.drop_all(bind=drop_create_engine)


def drop_create():
    drop_tables()
    create_tables()


drop_create()
