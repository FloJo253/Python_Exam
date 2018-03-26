from django.conf.urls import url   
from . import views          

urlpatterns = [     
    url(r'^$', views.main), 
    url(r'^/users/(?P<item_id>\d+)$', views.user), 
    url(r'^/create', views.create),
    url(r'^/fav/(?P<item_id>\d+)$', views.favorite), 
    url(r'^/remove/(?P<item_id>\d+)$', views.remove), 
    ]