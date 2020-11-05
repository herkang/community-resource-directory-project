""" Models for minority community resource directory """

from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()
""" Creates a SQLAlchemy instance at the variable db """

class User(db.Model):
""" Creates a User """

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, 
                        primary_key=True, 
                        autoincrement=True)
    username = db.Column(db.String, nullable=False, unique= True)
    password = db.Column(d.String)
