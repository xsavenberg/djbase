from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'change_this_to_an_actual_secret_key_before_deploy!'

DEBUG = env.bool('DJANGO_DEBUG', default=True)