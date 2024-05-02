from backend.db.session_maker import Session
from backend.db.models.model_user import User
from sqlalchemy import update


def update_user(id, info: dict[str: str]):
    stmt = (
        update(User)
        .where(User.id == id)
        .values(info)
    )
    with Session() as session:
        session.execute(stmt)
        session.commit()


# user = {'username': 'Aleks'}
# id = "491e584c-559b-4f55-a13e-965c7db3c450"
# update_user(id, user)
