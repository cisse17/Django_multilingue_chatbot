# Projet Diot-SIACI Django Multilingue avec Chatbot ...

## Description

Ce projet est une application Django multilingue avec une fonctionnalité de blog et un chatbot intégré utilisant l'API OpenAI.

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre système :

- Python 3.11.2
- pip
- virtualenv  (pour la création de votre environnement virtuel)
- [gettext](https://www.gnu.org/software/gettext/) (pour l'internationalisation)
- [Git](https://git-scm.com/) creer un compte github et installer git pour les commandes git.

## Installation

1. **Clonez le dépôt :**

   ```bash
   git clone https://github.com/votre-utilisateur/votre-repo.git
   cd votre-repo

## Créez un environnement virtuel et activez-le
- python -m venv env
- source env/bin/activate  # Sur Windows tapez cette commande avec le nom de votre environnement      virtuel : env\Scripts\activate

## Installez les dépendances :
- Ce requirements.txt permet d'installer tous les modules installer pour ce projet
- pip install -r requirements.txt

## Configurez les variables d'environnement :
- Créez un fichier .env à la racine du projet et ajoutez vos clés API et autres configurations nécessaires :
    SECRET_KEY=votre_secret_key
    DEBUG=True
    ALLOWED_HOSTS=127.0.0.1, .localhost
    OPENAI_API_KEY=votre_cle_api_openai

## Appliquez les migrations :
- python manage.py migrate

## Créez un super utilisateur pour accéder à l'admin Django :
- python manage.py createsuperuser

## Vous pouvez collectez les fichiers statiques en tapant cette ligne de commande
- python manage.py collectstatic

## Internationalisation (i18n)
1. Créer les fichiers de traduction en tapant ces commandes 
- python manage.py makemessages -l fr
- python manage.py makemessages -l en

2. Compilez les fichiers de traduction :
- python manage.py compilemessages  

3. Utilisation de Rosetta et django-parler :
- Ajoutez rosetta et parler à votre fichier INSTALLED_APPS dans settings.py et accédez à /rosetta/ pour gérer les traductions.  
- Ajoutez rotessa avant dans votre main url: path('rosetta/', include('rosetta.urls')),

## Lancer le Serveur de Développement
1. Démarrez le serveur Django :
- python manage.py runserver

2. Accédez à l'application :
- Ouvrez votre navigateur et allez à http://127.0.0.1:8000.

## Fonctionnalités
### Blog
- Ajoutez, éditez et supprimez des articles de blog via l'interface d'administration Django.

### Chatbot
- Le chatbot est accessible via l'URL /chatbot/. Vous pouvez lui poser des questions et obtenir des réponses générées par le modèle OpenAI.

### Multilang
- Pour le changement de la langue de l'interface utilisateur. (Au niveau de la page d'accueil )

## Déploiement
- Vous pouvez déployer cette application sur des plateformes telles que Render.com, Heroku, pythonanywhere ou tout autre hébergeur supportant Django.

## Assurez-vous de remplacer les placeholders comme `votre-utilisateur`, `votre-repo`, et `votre_cle_api_openai` par les informations réelles de votre projet. Ce fichier `README.md` offre des instructions détaillées pour installer, configurer et exécuter votre application Django. 


