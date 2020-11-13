
run-docker-compose-command:
	docker-compose ${command}
dc: run-docker-compose-command

build-image: command=build make-migrations migrate web celery
build-image: dc

make-migrations: command=run make-migrations
mm: makemigrations

migrate: command=run migrate
migrate: dc

run: command=up web celery flower
run: dc

test: command=run tests
test: dc

bash: command=run --rm web sh
bash: dc

build:
	make build-image
	make migrate
