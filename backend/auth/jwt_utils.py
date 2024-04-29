import jwt
from jwt.exceptions import InvalidSignatureError

secret = 'secret_key'


async def get_jwt(user):
    payload = user
    try:
        encoded_jwt = jwt.encode(payload, secret, algorithm='HS256')
    except InvalidSignatureError:
        return 'error'
    return encoded_jwt

