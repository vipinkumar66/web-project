from datetime import datetime
from first_web import db, login_manager, app
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))





class User(db.Model, UserMixin):
    id= db.Column(db.Integer, primary_key= True)
    username= db.Column(db.String(20), unique=True, nullable=False)
    email= db.Column(db.String(120), nullable=False, unique=True)
    image_file= db.Column(db.String(20), nullable=False, default='default.png')
    password= db.Column(db.String(60), nullable=False, unique=True)
    posts= db.relationship('Post', backref='author', lazy=True)



    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"


class Post(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(20), nullable=False)
    content= db.Column(db.Text, nullable=False)
    date_posted= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
            return f"Post('{self.title}', '{self.date_posted}')"