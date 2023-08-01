# Utilisez l'image Python officielle comme image de base
FROM python:3.9

# Copiez les fichiers de l'application dans le conteneur
WORKDIR /app
COPY app.py /app/app.py
COPY templates /app/templates
COPY requirements.txt /app/requirements.txt

# Installez les dépendances de l'application
RUN pip install --no-cache-dir -r /app/requirements.txt

# Exposez le port 5000 sur le conteneur
EXPOSE 5000

# Démarrez l'application lorsque le conteneur est lancé
CMD ["python", "app.py"]