from setuptools import setup

setup(name='aplicacion',
	version='0.1',
	description='Web application about polls',
	url='https://github.com/javiexfiliana7/submodulo-javi',
	author='Javier Ruiz César',
	author_email='javiexfiliana@gmail.com',
	license='GNU GPL',
	packages=['aplicacion'],
	install_requires=['django','wheel'],
	zip_safe=False)
