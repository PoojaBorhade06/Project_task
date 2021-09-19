import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Pro1.settings')
import django
django.setup()

from .models import Studentdata

from faker import Faker
from random import *
faker=Faker()

