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

# Encuestas sitio web:

Aplicación que nos permite crear y votar encuestas. Para realizarla hemos seguido el tutorial de [Django](https://docs.djangoproject.com/en/1.8/intro/tutorial01/) , y la hemos usado para avanzar en la asignatura de Infraestructura Virtual y Desarrollo de Aplicaciónes de Internet.

##Uso

Una vez descargada la aplicación, nos vamos a **submodulo-javi-master/aplicacion/pollaplication/** y lo ejecutamos en la terminal con **python manage.py runserver**:

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

Mi makefile es [este](/aplicacion/pollaplication/Makefile):

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


Mi archivo tests.py está [aquí](aplicacion/pollaplication/polls/tests.py). Ejemplo de ejecución:

![visualizacion](http://i67.tinypic.com/2q1ie6s.png)

La funcionalidad inicial básica que presenta esta pequeña aplicación se piensa mantener para nuestro proyecto.

###Integración continua

Para la integración contínua hemos elegido [travis](https://travis-ci.org/) ya que es fácil de usar y entender.

En este apartado he creado un fichero llamado [setup.py](aplicacion/setup.py) y un fichero **.travis.ym**(el cual está en el directorio raíz).
Fichero [.travis.yml](/aplicacion/.travis.yml):

~~~
language: python
python:
 - "2.7"
# command to install dependencies
install:
 - python aplicacion/setup.py install
 - pip install -r aplicacion/requirements.txt
# command to run tests
script:
 - cd aplicacion/pollaplication
 - python manage.py test
~~~


Una vez creado estos dos archivos, con el Makefile y test.py también( de los apartados anteriores), realizamos los siguientes pasos:

- Registrarnos en la página de travis e indicar el repositorio que queremos que compruebe.
- En nuestro repositorio de github, en el apartado **Setting/Webhooks&services** tenemos que activar el apartado de **Travis**.

Saldrá algo así:

![travis](http://i63.tinypic.com/2pza06q.png)