## **Proyecto de IV(infraestructura Virtual junto con DAI(DESARROLO DE APLICACIONES DE INTERNET** ##



**Breve Descripción/Introducción:**

Breve Descripción/Introducción:

El proyecto consiste en una plataforma de compra/venta de productos on-line. La plataforma contiene varias secciones para la venta de todo tipo de productos. La plataforma consiste en una página web donde cualquiera podra ver los productos que se venden, pero para poder vender o comprar será necesario registro. Si el vendedor se encuentra conectado, cualquier comprador potencial podrá chatear con el para preguntarle sobre el productos.

Cada anuncio vendra acompañado de una foto y una descripcion del producto que se ajuste a la realidad. Cada producto deberá estar bien situado en su sección correspondiente.

Cada usuario podrá tener una lista de productos favoritos.

Habrá moderadores que podrán eliminar cualquier anuncio de material fuera de la ley o que no se ajuste a la política de la plataforma.

La plataforma albergará un foro donde poder opinar sobre las diferentes transacciones.

Este módulo se centrará en los servicios que el servidor de nuestro sistema web va a ofrecer. Conectaremos la aplicación con la base de datos, se procesarán todo lo relacionado con usuarios, anuncios, ventas, etc.. Y despliegue y configuración de la palicación. Usaremos Flask.

##Segundo hito
[![Build Status](https://travis-ci.org/javiexfiliana7/submodulo-javi.svg?branch=master)](https://travis-ci.org/javiexfiliana7/submodulo-javi)

# Encuestas sitio web:

Aplicación que nos permite crear y votar encuestas. Para realizarla hemos seguido el tutorial de [Django](https://docs.djangoproject.com/en/1.8/intro/tutorial01/) , y la hemos usado para avanzar en la asignatura de Infraestructura Virtual y Desarrollo de Aplicaciónes de Internet.

##Uso

Una vez descargada la aplicación, nos vamos a **submodulo-javi-master/pollaplication/** y lo ejecutamos en la terminal con **python manage.py runserver**:

![ejecucion](http://i68.tinypic.com/nvod8i.png)

Para votar encuestas ponemos en nuestro navegador **http://127.0.0.1:8000** donde nos aparecerán todas las preguntas que hayamos creado:

![cuestiones](http://i67.tinypic.com/2uesos4.png)

Seleccionamos una de las preguntas que aparecen:

![opciones](http://i63.tinypic.com/dbmm2w.png)

Tras esto, se almacenará nuestro voto:

![resultados](http://i65.tinypic.com/s24arm.png)


Para la creación de preguntas ejecutamos **python manage.py shell**, tal y como se explica en el [tutorial](https://docs.djangoproject.com/en/1.8/intro/tutorial01/) ( en el apartado **Playing with the API**):

![crear_pregunta](http://i66.tinypic.com/dzjk8z.png)

Y podemos ver la pregunta:

![visualizacion_de_la_pregunta](http://i67.tinypic.com/6xqec0.jpg)

##Herramienta de construcción:
Para este segundo apartado del hito vamos a crear un Makefile, con las siguientes opciones:

- clean: para borrar los archivos que se generan y no queremos. **make clean**

- install: instalará todo lo necesario para ejecutar la aplicación. **make install**

- test: que nos testeará la aplicación. **make test**

- run: nos ejecutará la aplicación. **make run**

- doc: nos generará la documentación. **make doc**

Mi makefile es [este](/pollaplication/Makefile):

~~~
#Makefile segundo hito 
#clean install test run doc

clean:
	- rm -rf *~*
	- find . -name '*.pyc' -exec rm {} \;

install: 
	python setup.py install
	
test: 
	python manage.py test
	
run:
	python manage.py runserver
doc:
	epydoc --html polls/*.py 
~~~

###Tests

Nos permiten comprobar la funcionalidad de los proyectos conforme los vamos desarrollando.

Los test están guardados en el archivo  **tests.py** , para ejecutarlos deberemos poner **python manage.py test**.


Mi archivo tests.py está [aquí](pollaplication/polls/tests.py). Ejemplo de ejecución:

![visualizacion](http://i67.tinypic.com/2q1ie6s.png)

La funcionalidad inicial básica que presenta esta pequeña aplicación se piensa mantener para nuestro proyecto.

###Integración continua

Para la integración contínua hemos elegido [travis](https://travis-ci.org/) ya que es fácil de usar y entender.

En este apartado he creado un fichero llamado [setup.py](setup.py) y un fichero **.travis.ym**(el cual está en el directorio raíz).
Fichero [.travis.yml](/.travis.yml):

~~~
language: python
python:
 - "2.7"
# command to install dependencies
install:
 - python setup.py install
 - pip install -r requirements.txt
# command to run tests
script:
 - cd pollaplication
 - python manage.py test
~~~


Una vez creado estos dos archivos, con el Makefile y test.py también( de los apartados anteriores), realizamos los siguientes pasos:

- Registrarnos en la página de travis e indicar el repositorio que queremos que compruebe.
- En nuestro repositorio de github, en el apartado **Setting/Webhooks&services** tenemos que activar el apartado de **Travis**.

Saldrá algo así:

![travis](http://i63.tinypic.com/2pza06q.png)


## Despliegue en un Paas
Esta práctica consiste en desplegar nuestra aplicación en un PaaS. Usaremos Heroku, debido a que es fácil, gratuito y permite usar python y el Framework Django. Para su despliegue modificaremos y crearemos los siguientes ficheros:

- Procfile, el cual indica a heroku que tiene que lanzar:
```
web: gunicorn pollaplication.wsgi --log-file -

```
- requirements.txt: especifica todo lo necesario para que nuestra aplicación funcione:
```
Django==1.8.6
argparse==1.2.1
dj-database-url==0.3.0
dj-static==0.0.6
django-toolbelt==0.0.1
djangorestframework==3.3.1
foreman==0.9.7
futures==3.0.3
gunicorn==19.3.0
psycopg2==2.6.1
requests==2.8.1
requests-futures==0.9.5
static3==0.6.1
wheel==0.26.0
whitenoise==2.0.4
wsgiref==0.1.2

```
Despues de esto nos registramos en Heroku. Una vez registrados ejecutaremos una serie de comandos que ahora se especifican, para lanzar nuestra aplicación en heroku:
```
wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh
heroku login
heroku create
git add .
git commit -m "upload v2
git push heroku master

```
La base de datos que usaremos en Heroku es **PostgreSQL**. Para ello:

- Tenemos *psycopg2* para poder usarla.
- También tenemos *dj_database_url*, necesario para PostgreSQL.
- Editamos el archivo *setting.py* del proyecto y añadimos lo siguiente( sacado del siguiente [enlace](http://stackoverflow.com/questions/26080303/improperlyconfigured-settings-databases-is-improperly-configured-please-supply):
```

import dj_database_url

...

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']
ON_HEROKU = os.environ.get('PORT')
if ON_HEROKU:
    DATABASE_URL='postgres://uhaxlowwnbgqrv:3decYI2il-srwwKVSDV6a4G-xQ@ec2-54-83-36-203.compute-1.amazonaws.com:5432/da2k9559f8odld'
    DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

.....

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


```

- En **wsgi.py** tendremos lo siguiente:
```
import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apuestas.settings")

#from whitenoise.django import DjangoWhiteNoise
application = get_wsgi_application()


application = Cling(get_wsgi_application())
#application = DjangoWhiteNoise(application)
```
- Destacar que en DATABASE_URL se indica la url que sale para la base de datos postgreSQL que Heroku nos ofrece, hay que darle a show para verlo.
- Guardamos cambios en github y hacemos **git push heroku master**.
- Ejecutamos los comando:
 **heroku run python manage.py makemigrations**
 **heroku run python manage.py migrate**
 **heroku run python manage.py createsuperuser**
 para sincronizar la base de datos PostgreSQL.

Aplicación [desplegada](https://secure-escarpment-5944.herokuapp.com/).

Se añade el proceso de integración continua con snap-ci, para ello:

- Nos registramos en  [https://snap-ci.com](https://snap-ci.com) y conectamos a nuestro repo.

![snap_pipeline](http://i64.tinypic.com/34y1cg4.png)

- Compruebamos que el repositorio esta conectado con **Github** y que tenemos el despliegue automático ( consultar pestaña Deploy ).

![github](http://i68.tinypic.com/2r553dk.png)

- Ahora, cada vez que realicemos un push a nuestro reopsitorio, se realizará un testeo previo a su posterior despliegue.


- Aquí tenemos la etiqueta de Snap-ci, de que todo ha ido correctamente.

[![Build Status](https://snap-ci.com/javiexfiliana7/submodulo-javi/branch/master/build_image)](https://snap-ci.com/javiexfiliana7/submodulo-javi/branch/master)


Con este último paso en snap-ci, hemos realizado la integración continua de la aplicación, cada vez que hagamos un push se pasarán los test y se desplegará la aplicación.

- Nota: **AVANCES**: se pueden ver en el [avances.md](avances.md).


