build:
	docker compose up

delete:
	docker compose rm composetest-redis-1
	docker compose rm composetest-web-1
	docker compose rmi redis
	docker compose rmi composetest-web

rebuild:
	make delete
	make build

