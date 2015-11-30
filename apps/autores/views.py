from django.views.generic import CreateView,TemplateView,ListView
from .models import Autor
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
import datetime
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from serializers import AutorSerializar

class RegistrarAutor(CreateView):
	template_name = 'autores/registrarAutor.html'
	model = Autor
	success_url = reverse_lazy('reportar_autor')

	

class ReportarAutor(ListView):
	template_name = 'autores/reportarAutor.html'
	model = Autor
	context_object_name = 'autores'

class JSONResponse(HttpResponse):
	"""
	An HttpResponse that renders its content into JSON.
	"""
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def Autores_lista(request):
	"""
	Lista todos los nombres de personas o la crea
	"""
	if request.method == 'GET':
		autores = Autor.objects.all()
		serializador = AutorSerializar(autores, many=True)
		return JSONResponse(serializador.data)
	
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializador = AutorSerializar(data=data)
		if serializador.is_valid():
			serializador.save()
			return JSONResponse(serializador.data, status=201)
		return JSONResponse(serializador.errors, status=400)

@csrf_exempt
def Autor_detalle(request, pk):
	"""
	Recuperar, actualizar o borrar una persona
	"""
	try:
		autor = Autor.objects.get(pk=pk)
	except Autor.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializador = AutorSerializar(autor)
		return JSONResponse(serializador.data)
	#elif request.method == 'PUT':
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializador = QuestionSerializar(autor, data=data)
		if serializador.is_valid():
			serializador.save()
			return JSONResponse(serializador.data,status=202)
		return JSONResponse(serializador.errors, status=400)
	elif request.method == 'DELETE':
		autor.delete()
		return HttpResponse(status=204)