from rest_framework import serializers
from onlineapp.models import Todolist, Todoitems

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todolist
        fields = ('id','name')

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todoitems
        todolist=serializers.IntegerField()
        fields=('id','description','iscomplete','dueDate','todolist')

