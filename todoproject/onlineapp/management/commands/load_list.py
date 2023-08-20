from django.core.management.base import BaseCommand, CommandError
from django.utils import termcolors
from onlineapp.models import Todoitems
from onlineapp.models import Todolist
import datetime
class Command(BaseCommand):
    def handle(self, *args, **options):
        name=raw_input("give a name for the input")
        list=Todolist()
        list.name=name
        list.save()