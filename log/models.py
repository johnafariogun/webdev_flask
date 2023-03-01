from log import db, bcrypt, login_manager
from flask_login import UserMixin
"""
To create a new entry in the database you create a python shell instance
then you run the following
`db.create_all()`
`from log.models import model_name`
`model_instance=Model(fields=field_input)`
`db.session.add()`

"""
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=50), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=300000)
    log = db.relationship('Log', backref='owned_user', lazy=True)

    def __repr__(self):
        return f'{self.username}'

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_password):
        self.password_hash = bcrypt.generate_password_hash(plain_password).decode('utf-8')

    def check_password(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)


class Log(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=300), nullable=False, unique=True)
    pick_up = db.Column(db.String(length=300), nullable=False)
    delivery = db.Column(db.String(length=300), nullable=False)
    description = db.Column(db.String(length=3000))
    shipping = db.Column(db.Integer(), nullable=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'{self.name}'