# -*- coding: utf-8 -*-

from uuid import uuid4
from datetime import datetime
from simplecrypt import encrypt, decrypt, DecryptionException

from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings
from . import logger

import sys

is_py2 = sys.version_info < (3, 0, 0)

if not is_py2:
    unicode = str

def decode_payer(enc):
    """ Декодирование пользователя-инициатора платежа """
    if enc is None:
        return
    try:
        return get_user_model().objects.get(pk=enc)
    except DecryptionException:
        logger.warn(u'Payer decryption error')
    except get_user_model().DoesNotExist:
        logger.warn(u'Payer does not exist')


def encode_payer(user):
    """ Кодирование пользователя-инициатора платежа """
    return str(user.id)

def number_generetor(view, form):
    """ Генератор номера платежа (по умолчанию) """
    if is_py2:
        uuid_fields = uuid4().get_fields()
    else:
        uuid_fields = uuid4().fields
    return u'{:%Y%m%d}-{:08x}'.format(datetime.now(), uuid_fields[0])

def get_request_data(request):
    """Получение данных, передаваемых с запросом"""
    if request.method == 'POST':
        return request.POST
    else:
        return request.GET


class CSRFExempt(object):
    """ Mixin отключения проверки CSRF ключа """

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(CSRFExempt, self).dispatch(*args, **kwargs)

