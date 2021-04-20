from app import db, bcrypt, login, app
from flask_login import UserMixin
from datetime import datetime
from hashlib import md5
from time import time
import jwt


class Admin(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, nullable=False)
    email = db.Column(db.String(120), index=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            app.config['SECRET_KEY'],
            algorithm='HS256'
        )

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token,
                            app.config['SECRET_KEY'],
                            algorithms='HS256'
                            )['reset_password']
        except:
            return
        return Admin.query.get(id)


# -------------------
# Articles
# -------------------
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, nullable=False)
    email = db.Column(db.String(120), index=True, nullable=False)
    comment = db.Column(db.String(300))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    allowed_comment = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Comment {self.id}, {self.username}, {self.comment}, {self.allowed_comment}>'

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)


class Article2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, nullable=False)
    email = db.Column(db.String(120), index=True, nullable=False)
    comment = db.Column(db.String(300))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    allowed_comment = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Comment {self.id}, {self.username}, {self.comment}, {self.allowed_comment}>'

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)


@login.user_loader
def load_user(id):
    return Admin.query.get(int(id))
