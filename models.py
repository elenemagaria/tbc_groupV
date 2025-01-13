from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from ext import db, login_manager


class BaseModel():

    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def save():
        db.session.commit()



class Product(db.Model, BaseModel):

    __tablename__ ="products"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    breed = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    img = db.Column(db.String(), nullable=True, default = "https://static.vecteezy.com/system/resources/thumbnails/009/292/244/small/default-avatar-icon-of-social-media-user-vector.jpg")
    contact =db.Column(db.String(), nullable=False, default = "No info available")

class User(db.Model, BaseModel, UserMixin):

    __tablename__ ="users"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    username = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    number = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)
    img = db.Column(db.String(), nullable=False, default = "https://static.vecteezy.com/system/resources/thumbnails/009/292/244/small/default-avatar-icon-of-social-media-user-vector.jpg")
    role = db.Column(db.String(), default="User")

    def __init__(self, username, email, name, number, img, password, role="User"):
        self.username = username
        self.name = name
        self.number = number
        self.img = img
        self.email = email
        self.password = generate_password_hash(password)
        self.role = role

    def check_password(self, password):
        return check_password_hash(self.password, password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
