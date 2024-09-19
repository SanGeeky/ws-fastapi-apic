up:
	docker compose up

down:
	docker compose down

build:
	docker compose build

bash:
	docker compose run --rm apic bash

test:
	docker compose run --rm apic pytest -v

env:
	python3 -m venv env

install:
	env/bin/pip3 install -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu

list:
	env/bin/pip3 list
