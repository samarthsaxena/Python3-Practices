# will be used for time expiration of token
from datetime import datetime
from flask import current_app
# Default implementation of all flask_login necessary methods
from flask_login import UserMixin
from flaskblog import db, login_manager
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


@login_manager.user_loader
def load_user(user_id):
    # in order to work with login manager, we'd need a mechanism to make login_manager aware of the schema and the way current_app queries the db
    return User.query.get(int(user_id))


# Now to define the db architecture, we'll just use Models from SQLAlchemy(i.e. class based structure)
class User(db.Model, UserMixin):
    """
    Represents model(db table structure) for any user's schema in the db
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(120), nullable=False, default='default.jpg')
    # Password will be hashed so the limit is quite okay
    password = db.Column(db.String(60), nullable=False)

    # IMP! relationship b/w User and Post is one to many, because a user can post multiple Posts
    # BUT a post can have only 1 author, so to define this we have posts relationship in User model
    posts = db.relationship('Post', backref='author',
                            lazy=True)  # backref is just to add the extra attribute to Post model, on the fly.

    # generate the token for reset password action
    def get_reset_token(self, expires_sec=1800):
        # 1800 is just 30 Min(s)
        s = Serializer(current_app.config.get('SECRET_KEY'), expires_sec)
        return s.dumps({'user_id': self.id}).decode('UTF-8')

    # Now to verify the legitimacy of token we need to have some logic in place here
    # this will be a static method for the current_app
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config.get('SECRET_KEY'))

        try:
            user_id = s.loads(token)['user_id']
        except:
            return None

        return User.query.get(user_id)

    # Override the __repr__ to know what's going on with the user object
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}', '{self.password}')"


# Now schema for Posts of the users
# IMP! relationship b/w User and Post is one to many, because a user can post multiple Posts
# BUT a post can have only 1 author, so to define this we have posts relationship in User model
class Post(db.Model):
    """
       Represents model(db table structure) for any Post's schema of a user in the db.
    """
    id = db.Column(db.Integer, primary_key=True)
    # Length of the title must not exceed 120 chars
    title = db.Column(db.String(120), nullable=False)
    # Post's date and time can be set to default i.e. system's datetime if not specified
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)  # Just passing the function as an argument rather executed result of that.
    content = db.Column(db.Text, nullable=False)
    # Add a foreign key to every post w.r.t. user id. The foreign key name used in this is in lower cases because
    # we're referring the table column name which is set to model's name in lower cases by default.(Not changing the
    # default nature)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    # Override the __repr__ to know what's going on with the user object
    def __repr__(self):
        return f"Post('{self.id}', '{self.title}', '{self.date_posted}', '{self.content}')"
