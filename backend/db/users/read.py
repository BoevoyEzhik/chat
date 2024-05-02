from backend.db.session_maker import Session
from backend.db.models.model_user import User


def read_user(email) -> User:
    with Session() as session:
        return session.query(User).where(User.email == email).first()

