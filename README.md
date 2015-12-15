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


##Herramienta de construcción:
Para este segundo apartado del hito vamos a crear un Makefile, con las siguientes opciones:

- clean: para borrar los archivos que se generan y no queremos. **make clean**

- install: instalará todo lo necesario para ejecutar la aplicación. **make install**

- test: que nos testeará la aplicación. **make test**

- run: nos ejecutará la aplicación. **make run**

Mi makefile es [este](/Makefile):

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
Vamos a desplegar nuestra aplicación en un PaaS. Nos registramos en Heroku que es el que se va a usar. Añadimos lo siguiente:

- requirements.txt: especifica todo lo necesario para que nuestra aplicación funcione:
```
Django==1.8.6
django-toolbelt==0.0.1
djangorestframework==3.3.1
dj-database-url==0.3.0
dj-static==0.0.6
gunicorn==19.3.0
static3==0.6.1
wheel==0.24.0
whitenoise==2.0.4
psycopg2==2.6.1
Pygments==2.0.2

```

- Procfile, el cual indica a heroku que tiene que lanzar:
```
web: gunicorn pollaplication.wsgi --log-file -

```

La base de datos que usaremos en Heroku es **PostgreSQL**. Para ello:

- Tenemos *psycopg2* para poder usarla.
- También tenemos *dj_database_url*, necesario para PostgreSQL.
- Editamos el archivo *setting.py* y añadimos lo siguiente( sacado del siguiente [enlace](http://stackoverflow.com/questions/26080303/improperlyconfigured-settings-databases-is-improperly-configured-please-supply):

![setting](http://i68.tinypic.com/30thuvp.jpg)

- En **wsgi.py** tendremos lo siguiente:
![wsgi](http://i67.tinypic.com/30nav6f.png)


Lanzamos la aplicación en heroku:

```
wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh
heroku login
heroku create
git add .
git commit -m "upload v2
git push heroku master

```

- Guardamos cambios en github y hacemos **git push heroku master**.
- Para sincronizar la base de datos PostgreSQL ejecutamos los comando:
 **heroku run python manage.py makemigrations**
 **heroku run python manage.py migrate**
 **heroku run python manage.py createsuperuser**

Aplicación [desplegada](https://serene-dawn-1237.herokuapp.com/).

Añadimos el proceso de integración continua con snap-ci, para ello vamos a seguir los siguientes pasos:

[![Build Status](https://snap-ci.com/javiexfiliana7/submodulo-javi/branch/master/build_image)](https://snap-ci.com/javiexfiliana7/submodulo-javi/branch/master)

- Nos registramos en  [https://snap-ci.com](https://snap-ci.com) y conectamos a nuestro repositorio.

![snap_pipeline](http://i64.tinypic.com/34y1cg4.png)

- Comprobamos que el repositorio esta conectado con **Github** y que tenemos el despliegue automático ( consultar pestaña Deploy ).

![github](http://i68.tinypic.com/2r553dk.png)

- Ahora, cada vez que realicemos un push a nuestro reopsitorio, se realizará un testeo previo a su posterior despliegue.


Hemos añadido un archivo **.sh** para realizar el despligue de la aplicacion, puede verse [aquí](despliegue.sh). Para realizarlo nos hemos servido del siguiente [enlace](https://github.com/iblancasa/BackendSI2-IV/wiki/DespliegueHeroku), el cual nos conducía a otros enlaces de heroku, los cuales hemos usado para contrastar ideas.

