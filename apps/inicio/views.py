from django.views.generic import TemplateView,FormView
from .forms import UserForm
from models import Perfiles
from django.core.urlresolvers import reverse_lazy
from .models import Perfiles
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from serializers import PerfilesSerializar


class Registrarse(FormView):
	template_name = 'inicio/registrarse.html'
	form_class = UserForm
	success_url = reverse_lazy('registrarse')

	def form_valid(self, form):
		user = form.save()
		perfil = Perfiles()
		perfil.usuario = user
		perfil.telefono = form.cleaned_data['telefono']
		perfil.save()
		return super(Registrarse , self).form_valid(form)
	
class JSONResponse(HttpResponse):
	"""
	An HttpResponse that renders its content into JSON.
	"""
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def Perfiles_lista(request):
	"""
	Lista todos los nombres de personas o la crea
	"""
	if request.method == 'GET':
		perfiles = Perfiles.objects.all()
		serializador = PerfilesSerializar(perfiles, many=True)
		return JSONResponse(serializador.data)
	
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializador = PerfilesSerializar(data=data)
		if serializador.is_valid():
			serializador.save()
			return JSONResponse(serializador.data, status=201)
		return JSONResponse(serializador.errors, status=400)

@csrf_exempt
def Perfiles_detalle(request, pk):
	"""
	Recuperar, actualizar o borrar una persona
	"""
	try:
		perfiles = Perfiles.objects.get(pk=pk)
	except Perfiles.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializador = PerfilesSerializar(perfiles)
		return JSONResponse(serializador.data)
	#elif request.method == 'PUT':
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializador = QuestionSerializar(perfiles, data=data)
		if serializador.is_valid():
			serializador.save()
			return JSONResponse(serializador.data,status=202)
		return JSONResponse(serializador.errors, status=400)
	elif request.method == 'DELETE':
		perfiles.delete()
		return HttpResponse(status=204)