"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import datetime

from django.utils import timezone
from django.test import TestCase

from models import Perfiles

# Create your tests here.
from rest_framework import status
from rest_framework.test import APITestCase

class RutasTests(APITestCase):

    def Autor(self):
        q1 = Perfiles(usuario='Lorenzo',telefono='653057946')
        q1.save()
        self.assertEqual(response.content,'{"usuario":"Lorenzo","telefono":"653057946"}')
        print("Question consultada XD2")

    def test_detalle_varios_autores(self):
        q1 = Perfiles(usuario='Lorenzo' , telefono='653057946')
        q1.save()
        q2 = Perfiles(usuario='Manuel' , telefono='653057946')
        q2.save()
        response = self.client.get('/perfileslist/')
        self.assertEqual(response.content,'[{"usuario":"Lorenzo","telefono":"653057946"},{"usuario":"Manuel","telefono":"653057946"}]')
        print("Varias personas consultadas en detalle correctamente1")
