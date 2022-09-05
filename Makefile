SHELL=/bin/bash -e -o pipefail
PROJECT ?= recipe-app-api
PROJECT_VERSION ?= local
COMPOSE_FILE=docker-compose.yml
DC=docker-compose -p ${PROJECT} -f ${COMPOSE_FILE}

DOCKERFILE=Dockerfile

export USER_ID=$(shell id -u)
export GROUP_ID=$(shell id -g)

.DEFAULT_GOAL := help

.PHONY: help
#COLORS
GREEN  := $(shell tput -Txterm setaf 2)
WHITE  := $(shell tput -Txterm setaf 7)
YELLOW := $(shell tput -Txterm setaf 3)
RESET  := $(shell tput -Txterm sgr0)

HELP_FUN = \
    %help; \
    while(<>) { push @{$$help{$$2 // 'options'}}, [$$1, $$3] if /^([a-zA-Z0-9\-_]+)\s*:.*\#\#(?:@([a-zA-Z0-9\-_]+))?\s(.*)$$/ }; \
    print "usage: make [target]\n\n"; \
    for (sort keys %help) { \
    print "${WHITE}$$_:${RESET}\n"; \
    for (@{$$help{$$_}}) { \
    $$sep = " " x (55 - length $$_->[0]); \
    print "  ${YELLOW}$$_->[0]${RESET}$$sep${GREEN}$$_->[1]${RESET}\n"; \
    }; \
    print "\n"; }

.PHONY: help
help: ##@other Show this help.
	@perl -e '$(HELP_FUN)' $(MAKEFILE_LIST)


.PHONY: build
build: ##@development Build containers. Needed only after changes in requirements.
build: args?= -f Dockerfile
build: target?= development
build:
	docker-compose build

.PHONY: server
server: ##@development Start an API instance.
	${DC} up

.PHONY: djshell
djshell: ##@development Starts a shell plus instance.
	${DC} run --rm app sh -c "python manage.py shell_plus"

.PHONY: test
test: ##@test Run tests for the project.
	${DC} run --rm app sh -c "python manage.py test"

.PHONY: djhelp
djhelp: ##@development Prints django-manage help.
	${DC} run --rm app sh -c "python manage.py help"
