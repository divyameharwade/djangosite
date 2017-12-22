from django.conf.urls import  url
from .views import list_stuff, create_stuff, edit_stuff, delete_stuff, thing_detail

urlpatterns = [
    url(r'^$',list_stuff, name='list-stuff'),
    url(r'^(?P<thing_id>\d+)/$', thing_detail, 
        name='thing-detail'),
    url(r'^create/$', create_stuff,
        name='create-stuff'),
    url(r'^edit/(?P<thing_id>\d+)/$', edit_stuff,
        name='edit-stuff'),
    url(r'^delete/(?P<thing_id>\d+)/$', delete_stuff,
        name='delete-stuff'), 
]    
