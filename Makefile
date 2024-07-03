migrate:
	python manage.py makemigrations
	python manage.py migrate

start:
	python manage.py runserver
