default:
	cat Makefile


migrate:
	cd project && python manage.py migrate

run:
	cd project && python manage.py runserver


