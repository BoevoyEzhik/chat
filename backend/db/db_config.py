dialect = 'postgresql'
driver = 'psycopg2'
user = 'chat'
password = 'chat'
host = 'chat-db'
dbname = 'chat'

db_url = f'{dialect}+{driver}://{user}:{password}@{host}/{dbname}'
