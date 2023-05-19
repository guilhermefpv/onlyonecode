#
# Reference Guide - https://www.gnu.org/software/make/manual/make.html
#

# Build-time
all: build-flask-prod test
.PHONY: build-flask-prod test
# Step to build docker image of flask-prod
build-flask-prod:
	@echo "------------------"
	@echo "--> Building flask-prod a docker container image"
	@echo "------------------"
	docker-compose build

logs:
	@echo "------------------"
	@echo "--> Logging flask-prod a docker container"
	@echo "------------------"
	@docker-compose logs --tail 30 --follow flask-prod

logs-nginx:
	@echo "------------------"
	@echo "--> Log flask-prod a docker container"
	@echo "------------------"
	@docker-compose logs --tail 30 --follow nginx

run:
	@echo "------------------"
	@echo "--> Running flask-prod docker image"
	@echo "------------------"
	@docker-compose up -d

run-build:
	@echo "------------------"
	@echo "--> Building flask-prod docker image"
	@echo "------------------"
	@docker-compose up --build -d

test:
	@echo "------------------"
	@echo "--> Running Tests/Linter"
	@echo "------------------"
	@docker-compose run --rm manage lint; docker-compose run --rm manage test