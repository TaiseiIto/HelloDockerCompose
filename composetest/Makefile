.PHONY: compose
compose:
	docker compose up

.PHONY: decompose
decompose:
	if [ -n "$$(docker ps -a --format {{.Names}} | grep composetest-redis-1)" ]; then docker rm composetest-redis-1; fi
	if [ -n "$$(docker ps -a --format {{.Names}} | grep composetest-web-1)" ]; then docker rm composetest-web-1; fi
	if [ -n "$$(docker images --format {{.Repository}}:{{.Tag}} | grep redis:alpine)" ]; then docker rmi redis:alpine; fi
	if [ -n "$$(docker images --format {{.Repository}}:{{.Tag}} | grep composetest-web:latest)" ]; then docker rmi composetest-web:latest; fi

.PHONY: recompose
recompose:
	make decompose
	make compose

.PHONY: watch
watch:
	make decompose
	docker compose watch

