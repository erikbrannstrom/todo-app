from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^create/$', 'auth.views.create'),
    (r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'tmpl/login.html'}),
    (r'^logout/$', 'django.contrib.auth.views.logout_then_login', {'login_url': '/account/login'}),
)