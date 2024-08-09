import os

# instance/config.py
SECRET_KEY = SECRET_KEY = os.getenv("SECRET_KEY")
SQLALCHEMY_DATABASE_URI = "mysql://user:password@localhost/db_name"
