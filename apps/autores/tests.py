"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import datetime

from django.utils import timezone
from django.test import TestCase

from models import Autor

# Create your tests here.
from rest_framework import status
from rest_framework.test import APITestCase

class RutasTests(APITestCase):

    def Autor(self):
        q1 = Autor(nombre='Cervantes',pais='Espania',descripcion='Hola',foto='http://localhost:8000/media/foto_autor/220px-Cervantes_Valladolid_lou.jpg')
        q1.save()
        self.assertEqual(response.content,'{"nombre":"Cervantes","pais":"Espania","descripcion":"Hola","foto":"http://localhost:8000/media/foto_autor/220px-Cervantes_Valladolid_lou.jpg"}')
        print("Question consultada XD1")

    def test_detalle_varios_autores(self):
        q1 = Autor(nombre='Vargas' , pais='Colombia',descripcion='Escritor',foto='foto1')
        q1.save()
        q2 = Autor(nombre='Vargas(2)' , pais='Colombia(2)',descripcion='Escritor(2)',foto='foto2')
        q2.save()
        response = self.client.get('/autor/autoreslist/')
        self.assertEqual(response.content,'[{"nombre":"Vargas","pais":"Colombia","descripcion":"Escritor","foto":"http://localhost:8000/media/foto1"},{"nombre":"Vargas(2)","pais":"Colombia(2)","descripcion":"Escritor(2)","foto":"http://localhost:8000/media/foto2"}]')
        print("Varias personas consultadas en detalle correctamente2")



