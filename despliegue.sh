git clonehttps://github.com/javiexfiliana7/proyectoDAI-IV.git
cd proyectoDAI-IV
pwd
heroku keys:add
heroku git:clone -a tango_with_django_project
heroku ps:scale web=1 --app tango_with_django_project
heroku open --app tango_with_django_project
