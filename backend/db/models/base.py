from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, Uuid, MetaData
from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy.sql import func
from uuid import uuid4


class _BaseModel:
    id = Column(Uuid, primary_key=True, default=uuid4())
    cdate = Column(DateTime, nullable=False, default=func.now())
    udate = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())


convention = {
    'all_column_names': lambda constraint, table: '_'.join([
        column.name for column in constraint.columns.values()
    ]),
    'ix': 'ix__%(table_name)s__%(all_column_names)s',
    'uq': 'uq__%(table_name)s__%(all_column_names)s',
    'ck': 'ck__%(table_name)s__%(constraint_name)s',
    'fk': 'fk__%(table_name)s__%(all_column_names)s__%(referred_table_name)s',
    'pk': 'pk__%(table_name)s',
}

"""
В значениях параметра naming_convention можно указать шаблон,
который состоит из типа индекса/constraint (ix/uq/fk и др.) и названия таблицы,
разделенных подчеркиваниями.
В каких-то шаблонах можно перечислить еще и все столбцы.
Например, для primary-ключа этого делать не обязательно, можно указать просто название таблицы.

Когда вы начинаете делать новый проект, то один раз добавляете в него шаблоны наименований и забываете.
С тех пор все миграции у вас генерируются с одинаковыми названиями индексов и constraint'ов.

Это важно и по другой причине: когда вы решите, что в вашей объектной модели этот индекс больше не нужен и удалите его,
то Alembic будет знать, как он называется, и правильно сгенерирует миграцию.
Это уже некий залог надежности, что все будет работать, как должно.
"""

metadata_obj = MetaData(naming_convention=convention)

BaseDBModel: DeclarativeMeta = declarative_base(cls=_BaseModel, metadata=metadata_obj)
