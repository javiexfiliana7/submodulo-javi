#Makefile FJGM segundo hito 
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
	epydoc --html apu/*.py 