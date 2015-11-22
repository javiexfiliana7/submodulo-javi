import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question, Choice

# Create your tests here.
from rest_framework import status
from rest_framework.test import APITestCase
from polls.views import *

class RutasTests(APITestCase):

    def test_pregunta_datail(self):
        q1 = Question(question_text='Other answer?' ,asunt='My other answer',descrip='My other answer',date='1993-05-19',pub_date='1993-05-19')
        q1.save()
        response = self.client.get('/preguntadetail/1/')
        self.assertEqual(response.content,'{"question_text":"Other answer?","asunt":"My other answer","descrip":"My other answer","date":"1993-05-19"}')
        print("Question consultada XD")

    def test_detalle_varias_personas(self):
        q1 = Question(question_text='Other answer?' ,asunt='My other answer',descrip='My other answer',date='1993-05-19',pub_date='1993-05-19')
        q1.save()
        q2 = Question(question_text='Other answer(2)?' ,asunt='My other answer(2)',descrip='My other answer(2)',date='1993-05-19(2)',pub_date='1993-05-19')
        q2.save()
        response = self.client.get('/preguntalist/')
        self.assertEqual(response.content,'[{"question_text":"Other answer?","asunt":"My other answer","descrip":"My other answer","date":"1993-05-19"},{"question_text":"Other answer(2)?","asunt":"My other answer(2)","descrip":"My other answer(2)","date":"1993-05-19(2)"}]')
        print("Varias personas consultadas en detalle correctamente")

class QuestionMethodTests(TestCase):

	def test_create_question(self):
		q = Question(question_text = "Test question",pub_date=timezone.now())

		q.save()

		c = Choice(question = q , choice_text = "Choice test 1", votes=2)

		c.save()

		c = Choice(question = q , choice_text = "Choice test 2", votes=6)

		c.save()

		c = Choice(question = q , choice_text = "Choice test 3", votes=8)

		c.save()

		
		self.assertEqual(q.question_text, "Test question")

	def test_was_published_recently_with_future_question(self):
 
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		self.assertEqual(future_question.was_published_recently(), False)











