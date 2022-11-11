import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','crudproject.settings')
import django
django.setup()
from crudapp.models import *
from faker import Faker
from random import *
fake=Faker()


def populate(n):
    for i in range(n):
      fno=randint(10,1001)
      fename=fake.name()
      fesal=randint(100000,150000)
      fearess=fake.city()


      emp_tab=Employee.objects.get_or_create(eno=fno,ename=fename,esal=fesal,eaddr=fearess)
populate(30)