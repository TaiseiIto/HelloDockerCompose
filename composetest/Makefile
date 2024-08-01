build:
	docker compose up

delete:
	if [ -n "$$(docker compose ps -a --format {{.Names}} | grep composetest-redis-1)" ]; then docker compose rm composetest-redis-1; fi
	if [ -n "$$(docker compose ps -a --format {{.Names}} | grep composetest-web-1)" ]; then docker compose rm composetest-web-1; fi
	if [ -n "$$(docker compose images --format {{.Repository}}:{{.Tag}} | grep redis:alpine)" ]; then docker compose rmi redis:alpine; fi
	if [ -n "$$(docker compose images --format {{.Repository}}:{{.Tag}} | grep composetest-web:latest)" ]; then docker compose rmi composetest-web:latest; fi

rebuild:
	make delete
	make build

