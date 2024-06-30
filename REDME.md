# Projet Diot-SIACI Django Multilingue avec Chatbot ...

## Description

Ce projet est une application Django multilingue avec une fonctionnalité de blog et un chatbot intégré utilisant l'API OpenAI.

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés sur votre système :

- Python 3.11.2
- pip
- virtualenv  (pour la création de votre environnement virtuel)
- [gettext](https://www.gnu.org/software/gettext/) (pour l'internationalisation)
- Attention pour l'installation de gettext si vous en avez pas vous pouvez confronter des erreurs comme  CommandError: Can't find msguniq dans ce  cas pensez à téléchargé les binaires précompilés  sur le site de GNU gettext qui propose des binaires Windows pour gettext.
- choisissez un répertoire pour le téléchargement et ajoutez le chemin de votre répertoire du dossier télécharger dans votre variable d'environnement
- Ouvrez un terminal et tapez cette commande pour voir si vous l'avez bien installer  
 msguniq --version

- [Git](https://git-scm.com/) creer un compte github et installer git pour les commandes git.

## Installation

1. **Clonez le dépôt :**

   ```bash
   git clone https://github.com/votre-utilisateur/votre-repo.git
   cd votre-repo

## Créez un environnement virtuel et activez-le

- Tapez ces commandes 

- python -m venv env 

- source env/bin/activate Sur Windows tapez cette commande avec le nom de votre environnement      virtuel : env\Scripts\activate


## Installez les dépendances :
- Ce requirements.txt permet d'installer tous les modules installer pour ce projet

- pip install -r requirements.txt


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

3. Installation et Utilisation de Rosetta et django-parler :

- pip install django-parler
- pip install django-rosetta

- Ajoutez rosetta et parler à votre fichier INSTALLED_APPS dans settings.py et accédez à /rosetta/ pour gérer les traductions.  
- Ajoutez rosetta avant dans votre main url: path('rosetta/', include('rosetta.urls')),

## Lancer le Serveur de Développement
1. Démarrez le serveur Django :
- python manage.py runserver

2. Accédez à l'application :
- Ouvrez votre navigateur et allez à http://127.0.0.1:8000.
- Vous pouvez acceder à l'admin en faisant http://127.0.0.1:8000/admin et conecter avec vos informations lors de la création de superuser

## Fonctionnalités

### Blog
- Ajoutez, éditez et supprimez des articles de blog via l'interface d'administration Django.

### Chatbot
- Le chatbot est accessible via l'URL /chatbot/. Vous pouvez lui poser des questions et obtenir des réponses générées par le modèle OpenAI.

### Multilingue
- Pour le changement de la langue de l'interface utilisateur. (Au niveau de la page d'accueil ) à améliorer

## Déploiement
- Vous pouvez déployer cette application sur des plateformes telles que Render.com, Heroku, pythonanywhere ou tout autre hébergeur supportant Django.
- Attention il pourrait arriver des bugs lors du déploiement (du temps à prévoir pour le déploiement en rapport avec le deadline si vous avez un deadline à respecter).

## Configurez les variables d'environnement :
- Créez un fichier .env à la racine du projet et ajoutez vos clés API et autres configurations nécessaires :
    SECRET_KEY=votre_secret_key
    DEBUG=True
    ALLOWED_HOSTS=127.0.0.1, .localhost 
    OPENAI_API_KEY=votre_cle_api_openai

## NB : Utilisation de chatgpt
- Ce projet m'a pris à peu prés 7h30 de temps de travail selon mes disponibilités y compris la rédaction du doc. Mais En cas de probléme pour l'installation de gettext, probléme clé API, probléme de l'utilisation de django-parler, probléme de traduction  ou tout autre bug pensez revoir votre code et pour l'optimiser ou à utiliser chatgtp pour apporter des solutions mais comment l'utiliser pour avoir des réponses précises ? ceci dépend de toute personne. Important, Si c'est votre premiére fois vous réaliser ce genre de projet pensez à prendre ces suggestions pour eviter de prendre ce temps de travail.

- [lien du projet multilingue site chatbot](https://diotsiacichatbot.pythonanywhere.com/) 

- [Gestion du projet multilingue](https://trello.com/invite/b/rSJgJD7w/ATTI0bcd425dd6271c0e7ecf9975a82ece73B7F02773/conduite-de-projet-multilingue-diotsiaci)

- [Mes impréssions et compétences sur la réalisation de ce projet](https://docs.google.com/document/d/1wN9vfcqZ-mmyR1NrgX_i5IBHMWMfEsQ-IRiUCxEuGwU/edit#heading=h.uncwpjy325ei)

## Assurez-vous de remplacer les placeholders comme `votre-utilisateur`, `votre-repo`, et `votre_cle_api_openai` par les informations réelles de votre projet. Ce fichier `README.md` offre des instructions détaillées pour installer, configurer et exécuter votre application Django. 


