import os
import secrets

from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    # Ignore the name of original file, save the extension
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    # resize the picture before saving
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    # Save the compressed picture in profile_pics dir with random name
    i.save(picture_path)

    # Now return the name of the picture file from here
    # (i.e. to answer : what is the name of this user's profile picture)
    return picture_fn


# for sending email
def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@gmail.com',
                  recipients=[user.email])
    msg.body = f'''To Reset your password, Please visit the below link.

{url_for('users.reset_token', token=token, _external=True)}

<b> If you DID NOT make this request. Please ignore this mail! </b>
'''
    # send the mail
    mail.send(msg)
