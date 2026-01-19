import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'devsecret')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL', 
        'mysql+pymysql://root:MyStrongPass123!@localhost/notes_app'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

