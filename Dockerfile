FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /detect-grid-api

# Installer git et autres outils nécessaires
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Ajouter les fichiers locaux à l'image Docker
ADD . /detect-grid-api

# Mettre à jour pip et installer les dépendances Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Commande par défaut pour démarrer l'application
CMD ["python", "main.py"]
