from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from dis_site import db, loginManager

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password_hash = db.Column(db.String(80), unique=True, nullable=False)

    def hashPassword(self, password):
        self.password_hash = generate_password_hash(password=password, method="pbkdf2:sha256", salt_length=16)

    def checkPasswordHash(self, password):
        return check_password_hash(pwhash=self.password_hash, password=password)

    def __repr__(self):
        return '<User %r>' % self.password_hash

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

@loginManager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

