from base.models import Task
from django.db import connections,connection
from django.utils import timezone

def run():

    print(Task.objects.get(name='SQL').name)
    print(connection.queries)