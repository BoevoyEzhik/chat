.PHONY: . 								\
	help 								\
	tests								\

.DEFAULT_GOAL := help

help:  ## show all comands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

start:  ## run project
	docker compose up -d

stop:  ## stop project
	docker compose down

restart: stop start

rebuild:  ## rebuild project
	docker-compose down --remove-orphans && \
	docker-compose build --parallel && \
	docker-compose up -d

tests:  ## run tests in project
	pytest --cov

install-requirements:  ## install requirements
	pip install -r requirements.txt -c constaints.txt

install-all-requirements:  ## install all requirements
	pip install -r requirements.txt -r requirements.tests.txt -c constaints.txt

freeze-dependencies:  ## freeze dependencies
	pip freeze > constaints.txt