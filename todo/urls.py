from django.conf.urls.defaults import *

urlpatterns = patterns('todo.views',
    (r'^$', 'index'),
    (r'^(?P<id>\d+)/$', 'detail'),
    (r'^(?P<id>\d+)/add/$', 'add'),
)