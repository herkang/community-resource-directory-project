""" Models for minority community resource directory """

from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()
""" Creates a SQLAlchemy instance at the variable db """

class User(db.Model):
""" Creates an User object """

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, 
                        primary_key=True, 
                        autoincrement=True)
    username = db.Column(db.String, nullable=False, unique= True)
    password = db.Column(d.String)

    def __repr__(self):
        """ Show info about user"""
        
        return f'<User user_id={self.user_id} username={self.username}>'

class Resource(db.Model):
""" Creates a resource object """

    __tablename__ = 'resources'

    resource_id = db.Column(db.Integer, 
                            primary_key=True
                            autoincrement=True)
    resource_name = db.Column(db.String)
    