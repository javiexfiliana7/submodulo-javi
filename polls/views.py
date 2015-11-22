from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
import datetime
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from serializers import QuestionSerializar

from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


class JSONResponse(HttpResponse):
	"""
	An HttpResponse that renders its content into JSON.
	"""
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def Pregunta_lista(request):
	"""
	Lista todos los nombres de personas o la crea
	"""
	if request.method == 'GET':
		preguntas = Question.objects.all()
		serializador = QuestionSerializar(preguntas, many=True)
		return JSONResponse(serializador.data)
	
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializador = QuestionSerializar(data=data)
		if serializador.is_valid():
			serializador.save()
			return JSONResponse(serializador.data, status=201)
		return JSONResponse(serializador.errors, status=400)

@csrf_exempt
def Pregunta_detalle(request, pk):
	"""
	Recuperar, actualizar o borrar una persona
	"""
	try:
		pregunta = Question.objects.get(pk=pk)
	except Question.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializador = QuestionSerializar(pregunta)
		return JSONResponse(serializador.data)
	#elif request.method == 'PUT':
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializador = QuestionSerializar(persona, data=data)
		if serializador.is_valid():
			serializador.save()
			return JSONResponse(serializador.data,status=202)
		return JSONResponse(serializador.errors, status=400)
	elif request.method == 'DELETE':
		pregunta.delete()
		return HttpResponse(status=204)
