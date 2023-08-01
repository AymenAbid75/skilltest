# Commandes
PYTHON = python3
PIP = pip3
DOCKER = docker

# Cibles
run:
	$(PYTHON) app.py

install-dependencies:
	$(PIP) install -r requirements.txt

build-docker-image:
	$(DOCKER) build -t url-shortener-app .

run-docker-container:
	$(DOCKER) run -p 5000:5000 url-shortener-app

# Cible par défaut
.DEFAULT_GOAL := run