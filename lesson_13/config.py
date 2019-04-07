

#DEBUG = True
SECRET_KEY = 'should always be secret'

# Database settings:
#SQLALCHEMY_DATABASE_URI = r'sqlite:///C:\Иван\Python\Databases\MyBaseSqlLite\db.db3'
SQLALCHEMY_DATABASE_URI = 'postgresql://foxrec123:123@localhost/db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLED = False