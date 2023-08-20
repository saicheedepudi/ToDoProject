# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from onlineapp.models import Todoitems
from onlineapp.models import Todolist
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.
from rest_framework import generics


def viewList(request):
    result=Todolist.objects.all()
    item=Todoitems.objects.all()
    template = loader.get_template("onlineapp/listView.html")
    result = template.render(context={"lists": result,"items":item})
    return HttpResponse(result)
def deleteList(request):
    result = Todolist.objects.all()
    template = loader.get_template("onlineapp/DelView.html")
    result = template.render(context={"lists": result})
    return HttpResponse(result)

def itemList(request,name):
    result=Todoitems.objects.values().filter(todolist__name=name)
    template = loader.get_template("onlineapp/ItemView.html")
    result = template.render(context={"lists": result})
    return HttpResponse(result)

def totalView(request):
    result=Todolist.objects.all()
    li=[]
    for list in result:
        ans=Todoitems.objects.filter(todolist__name=list.name)
        li.append(ans)

    template = loader.get_template("onlineapp/TotalView.html")
    result = template.render(context={"lists": result,"items":li})
    return HttpResponse(result)

class ListCreateView(CreateView):
    model=Todolist
    fields=['name']
    success_url=reverse_lazy('onlineapp:lists')


class ListDeleteView(DeleteView):
    model=Todolist
    fields=['name']
    success_url = reverse_lazy('onlineapp:lists')

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from onlineapp.serializers import ItemSerializer, ListSerializer

@csrf_exempt
def lists_create(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        list = Todolist.objects.all()
        serializer = ListSerializer(list, many=True)

        return JsonResponse(serializer.data, safe=False)  #Controls if only ``dict`` objects may be serialized. Defaults to ``True``.

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
@csrf_exempt
def items_create(request,pk):

    list = Todolist.objects.get(pk=pk)

    if request.method == 'GET':
        item = Todoitems.objects.filter(todolist=pk)
        serializer = ItemSerializer(item, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def items_crud(request,pk):
    item = Todoitems.objects.get(pk=pk)
    if request.method == 'DELETE':
        item.delete()
        return HttpResponse(status=204)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def lists_crud(request, pk):
        list = Todolist.objects.get(pk=pk)
        if request.method == 'DELETE':
            list.delete()
            return HttpResponse(status=204)

#classbased views
class TODOList(generics.ListCreateAPIView):
    queryset = Todolist.objects.all()
    serializer_class = ListSerializer



#main view
def mainView(request):
    template=loader.get_template("onlineapp/MainView.html")
    result = template.render()
    return HttpResponse(result)

