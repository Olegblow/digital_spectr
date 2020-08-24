
make_migr:
	docker-compose run --rm web sh -c"flask db migrate

upgrade:
	docker-compose run --rm web sh -c"flask db upgrade"

ssh_web:
	docker-compose exec web sh

