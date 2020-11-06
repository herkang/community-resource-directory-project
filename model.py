""" Models for minority community resource directory """

from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy_utils import PhoneNumber 

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
        """ Show user informations """
        
        return f'<User user_id={self.user_id} username={self.username}>'

class Resource_category(db.Model):
""" Creates a resource category object"""

    __tablename__ = 'resource_categories'

    resource_category_id = db.Column(db.Integer, 
                        primary_key=True, 
                        autoincrement=True)
    resource_category_name = db.Column(db.String)

    def __repr__(self):
        """ Show user informations """
        
        return f'<Resource Category resource_category_id={self.resource_category_id} 
        Resource category name resource_category_name={self.resource_category_name}>'

class Resource(db.Model):
""" Creates a resource object """

    __tablename__ = 'resources'

    resource_id = db.Column(db.Integer, 
                            primary_key=True
                            autoincrement=True)
    resource_category_id = db.Column(db.Integer, 
                            db.ForeignKey('users.user_id'))
    resource_name = db.Column(db.String)
    # To do, add url to resource_name 
    # https://sqlalchemy-utils.readthedocs.io/en/latest/data_types.html#module-sqlalchemy_utils.types.phone_number

    service = db.Column(db.String)

    #phone_number = db.Column(db.String)
    # To do, limit to specific whole number input

    location = db.Column(db.String)
    #To do, figure out how to put location in from txt file
    
    resource = db.relationship('Resource_category', backref='resource_categories')

    def __repr__(self):
        """ Show user information """
        
        return f'<Resource resource_id={self.resource_id} resource name resource_name={self.resource_name}>'

class User_resource(db.Model):
""" Creates user's resource object"""

    __tablename__ = 'user_resources'

    user_resource = db.Column(db.Integer
                            primary_key=True, 
                            autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    resource_id = db.Column(db.Integer, db.ForeignKey('resources.resource_id'))
    
    user = db.relationship('User', backref='users')
    resource = db.relationship('Resource', backref='resources')

    saved_resources = db.Column(db.String)
    #To do, find correct way to store list of resources

    def __repr__(self):
        """ Show saved resources """
            return f'<Saved resources saved_resources={self.saved_resources}>'

