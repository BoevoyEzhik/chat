from backend.db.session_maker import Session
from backend.db.models.model_user import User


def create_user(info: dict[str: str]):
    with Session() as session:
        user = User(**info)
        session.add(user)
        session.commit()


# user = {'username': '112',
#         'password': '123',
#         'email': '123@123.ru'}
#
# create_user(user)
