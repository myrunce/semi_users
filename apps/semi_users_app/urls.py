from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users$', views.users),
    url(r'^users/new$', views.new_user),
    url(r'^users/create$', views.create),
    url(r'^users/(?P<user_id>\d+)$', views.show),
    url(r'^users/(?P<user_id>\d+)/edit$', views.edit),
    url(r'^users/(?P<user_id>\d+)/destroy$', views.delete),
]