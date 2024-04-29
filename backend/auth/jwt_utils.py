import jwt
from jwt.exceptions import InvalidSignatureError

secret = 'secret_key'


async def get_jwt():
    payload = {'id': "123",
               'username': "kek",
               'role': "user",
               }
    encoded_jwt = jwt.encode(payload, secret, algorithm='HS256')
    return encoded_jwt


# try:
#     s = jwt.decode(encoded_jwt, '123', algorithms=['HS256'])
# except InvalidSignatureError as e:
#     print(e)

async def process_jwt():
    pass
