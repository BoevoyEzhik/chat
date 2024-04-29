# from sqlalchemy import create_engine, MetaData, Table, Column, String, Uuid, DateTime
# from uuid import uuid4
# from datetime import datetime
# from db.db_config import db_url
#
# engine = create_engine(db_url, echo=True)
# meta = MetaData()
#
# user = Table(
#     'user', meta,
#     Column('id', Uuid, primary_key=True, default=uuid4()),
#     Column('email', String, unique=True, nullable=False),
#     Column('username', String),
#     Column('password', String),
#     Column('cdate', DateTime, default=datetime.now()),
#     Column('udate', DateTime, default=datetime.now())
# )
#
# meta.create_all(engine)
