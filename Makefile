migrate:
	python manage.py makemigrations
	python manage.py migrate

start:
	echo "Make sure that yuou have, installed all the requirements of the app"
	python manage.py runserver

start_docker:
	docker compose up