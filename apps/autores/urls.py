from django.conf.urls import patterns, include, url
from .views import RegistrarAutor,ReportarAutor


urlpatterns = patterns('', 
    url(r'^registrar/$' , RegistrarAutor.as_view() , name="registrar_autor"),
    url(r'^reportar/$' , ReportarAutor.as_view() , name="reportar_autor"),
	url(r'^autoreslist/$', 'apps.autores.views.Autores_lista'),
    url(r'^autordetail/(?P<pk>[0-9]+)/$', 'apps.autores.views.Autor_detalle'),

)
