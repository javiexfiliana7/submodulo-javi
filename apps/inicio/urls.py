from django.conf.urls import patterns, include, url
from .views import Registrarse

urlpatterns = patterns('',

	url(r'^$' , 'django.contrib.auth.views.login',
		{'template_name':'inicio/index.html'}, name='login'),

	url(r'^cerrar/$' , 'django.contrib.auth.views.logout_then_login',
		 name='logout'),

	url(r'^registrarse/$', Registrarse.as_view() , name = 'registrarse'),
	url(r'^perfileslist/$', 'apps.inicio.views.Perfiles_lista'),
    url(r'^perfilesdetail/(?P<pk>[0-9]+)/$', 'apps.inicio.views.Perfiles_detalle'),
)
