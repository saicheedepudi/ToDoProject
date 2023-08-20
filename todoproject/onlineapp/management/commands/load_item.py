from django.core.management.base import BaseCommand, CommandError
from django.utils import termcolors
from onlineapp.models import Todoitems
from onlineapp.models import Todolist
import datetime
class Command(BaseCommand):
    def handle(self, *args, **options):
        name=raw_input("give a name for the input")
        for i in range(0,5):
            c = Todolist.objects.filter(name=name)
            descrption=raw_input("enter the description for your item")
            duedate=raw_input("enter the due date")
            duedate=datetime.datetime.strptime(duedate, "%Y-%m-%d").date()
            obj=Todoitems()
            obj.description=descrption
            obj.dueDate=duedate
            obj.todolist=c[0]
            obj.save()






























