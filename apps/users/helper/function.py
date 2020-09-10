import uuid
from datetime import datetime
from django.core.mail import send_mail
import base64
import json


def get_unique_id(id=None):
    return uuid.uuid5(uuid.NAMESPACE_DNS, str(id) + str(datetime.now()))


def base64encode(user):
    dict = {}
    dict['token'] = user.password_reset_token
    dict['email'] = user.email
    dict = json.dumps(dict)
    encoded_dict = str(dict).encode('utf-8')
    base64_dict = base64.b64encode(encoded_dict)
    base64_dict_str = (str(base64_dict)).split("'")[1]
    return base64_dict_str


def send_reset_email(user, path=None, to = None):
    url_encoded_data = base64encode(user)
    url = path + "/auth/reset-password/?token=" + url_encoded_data

    subject = 'My Mantra - Reset Password'

    plain_message = 'Username - {} has a password resent link is {}.'.format(user.email,url)

    from_email = 'sheezan000.sheez@gmail.com'

    try:
        sent = send_mail(subject, plain_message, from_email, [to])
    except Exception as e:
        print(e)
        return  False
        pass
    return True