# from sqlalchemy import create_engine, MetaData
# from db.db_config import db_url
# from db.create import user
#
# engine = create_engine(db_url, echo=True)
# meta = MetaData()
#
#
# def insert_user(info: dict[str: str]):
#     info = dict(info)
#     print(info, type(info))
#     conn = engine.connect()
#     ins = user.insert().values(**info)
#     conn.execute(ins)
#     conn.commit()
