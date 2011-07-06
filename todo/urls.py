from django.conf.urls.defaults import *

urlpatterns = patterns('todo.views',
    (r'^$', 'index'),
    (r'^create/$', 'create'),
    (r'^(?P<id>\d+)/$', 'detail'),
    (r'^(?P<id>\d+)/add/$', 'add'),
    (r'^(?P<id>\d+)/move/$', 'move'),
)