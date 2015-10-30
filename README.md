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

###Tests

Los test nos permiten comprobar la funcionalidad de los proyectos conforme los vamos desarrollando.

Para ejecutarlos pondremos: **python manage.y test**.


Mi archivo tests.py está [aquí](aplicacion/pollaplication/polls/tests.py).

Este fichero es inicial, ayudado del tutorial de django, la funcionalidad inicial básica que presenta esta pequeña aplicación se piensa mantener para nuestro proyecto, por eso lo he añadido como trabajo de mi proyecto.

###Integración continua

Para la integración contínua usaremos travis [travis](https://travis-ci.org/) ya que es fácil de usar y entender( es similar a Shippable, que también lo he usado en los ejercicios).

Para poder usar travis:

-He creado un fichero llamado [setup.py](aplicacion/setup.py)

También he creado un fichero **.travis.ym**, el cual está en el directorio raíz.
Fichero travis.yml:

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


Una vez subido a github, e indicado travis que trabaje con repositorio correspondiente debe salir esto:

![travis](https://www.dropbox.com/s/uoyn00dq4dw8vph/img23.png?dl=1)
