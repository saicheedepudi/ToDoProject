from django.conf.urls import url
from django.views.generic import TemplateView
from onlineapp import views
app_name = 'onlineapp'

urlpatterns=[
url(r'^items/(?P<name>[a-zA-Z ]+)/$',views.itemList,name="itemDetails"),
url(r'^lists/$',views.viewList,name='lists'),
url(r'^totalView/$',views.totalView),
url(r'createlist/$',views.ListCreateView.as_view()),
url(r'deletelist/(?P<pk>[0-9]+)/$',views.ListDeleteView.as_view()),

url(r'^createList/(?P<pk>[0-9]+)/item/$',views.items_create),

url(r'^createList/$',views.lists_create),
url(r'^deleteItem/(?P<pk>[0-9]+)/$',views.items_crud),
url(r'^deleteList/(?P<pk>[0-9]+)/$',views.lists_crud),
# url(r'^homepage/$', TemplateView.as_view(template_name="onlineapp/ajax.html")),
# url(r'^homepage/template.html/$', TemplateView.as_view(template_name="onlineapp/template.html")),
# url(r'^homepage/template1.html/$', TemplateView.as_view(template_name="onlineapp/template1.html")),
url(r'^home/$',views.mainView)
]