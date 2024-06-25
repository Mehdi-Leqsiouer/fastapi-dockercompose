.PHONY : lint test

lint:
	isort src && black src && flake8 src
test:
	docker-compose exec -T backend pytest
