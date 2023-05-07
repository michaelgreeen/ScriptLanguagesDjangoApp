.PHONY: migrations build run requirements down remove prune

migrations:
	python manage.py makemigrations
	python manage.py migrate

# Build the Docker services
build:
	docker-compose build

# Run the Docker services
run:
	docker-compose up

# Generate requirements.txt
requirements:
	docker-compose run --rm django_app /bin/bash -c 'pip freeze > /app/requirements.txt'

# Stop and remove the Docker services
down:
	docker-compose down --rmi all --remove-orphans

# Remove all images
prune:
	docker images prune -a
