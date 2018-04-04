
from django.conf.urls import url
from . import views

app_name = 'photos'

urlpatterns =[
    #/photos
    url(r'^$', views.index, name='index'),
    #/photos/1
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #/photos/picture/add
    url(r'picture/add/$', views.PictureCreate.as_view(), name='picture-add'),
]