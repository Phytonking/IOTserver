from django.db import IntegrityError
from web.models import *
from uuid import uuid4
def create_session(use):
    try:
        ses = session.objects.create(session_id = uuid4(), user = u.objects.get(username=use), logged_out=False)
        ses.save()
    except IntegrityError:
        return False
    return ses.session_id

def logout_session(sess):
    try:
        k = session.objects.get(session_id=sess)
        try:
            us = k.user
            us.logged_in = False
            us.save()
            return True
        except u.DoesNotExist:
            return False
    except session.DoesNotExist:
        return False