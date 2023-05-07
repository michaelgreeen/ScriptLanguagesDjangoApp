.PHONY: build run requirements down remove prune

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

#Remove all images lol
prune:
	docker images prune -a