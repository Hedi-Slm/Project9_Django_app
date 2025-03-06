# LITRevu
LITRevu est une application web développée avec Django qui permet aux utilisateurs 
de demander ou de publier des revues/critiques de livres ou d'articles de littérature.

# Fonctionnalités
- **Inscription/Connexion** via une interface sécurisée
- **Créer des billets** pour demander des critiques sur un livre/article
- **Rédiger des critiques** en réponse aux billets ou de manière indépendante
- **Édition/suppression** de ses propres billets et critiques
- **Consulter son flux** :
  - Billets et critiques des autres utilisateurs suivis
  - Ses propres publications
  - Réponses à ses billets (même des non-followers)
- **Gestion des followers** :
    - Suivre d'autres utilisateurs
    - Ne plus suivre un utilisateur
    - Consulter la liste des utilisateurs suivis
    - Consulter la liste des utilisateurs suivants
- **Édition/suppression** de ses propres billets et critiques


# Prérequis

Python 3.8+ <br>
Django 3.2+ <br>
Pip

# Installation

1. Clonez ce dépôt sur votre machine locale a l'aide de la commande suivante : <br>
`git clone https://github.com/Hedi-Slm/Project9_Django_app`
2. Créez un environnement virtuel : <br>
`python -m venv env` <br>
3. Activez l'environnement virtuel : <br>
`env\Scripts\activate` pour Windows <br>
`source env/bin/activate` pour macOS/Linux <br>
4. Installez les dépendances : <br>
`pip install -r requirements.txt`
5. Effectuez les migrations de la base de données : <br>
`python manage.py migrate`
6. Lancez le serveur de développement : <br>
`python manage.py runserver`
7. Accédez à l'application via votre navigateur à l'adresse : http://127.0.0.1:8000/

# Utilisation

La base de données incluse dans ce dépôt contient déjà
des données de test pour vous permettre d'explorer l'application.
Vous pouvez vous connecter avec les identifiants suivants :

**Super-user** <br>
Nom d'utilisateur : root <br>
Mot de passe : root

**Utilisateur** <br>
Nom d'utilisateur : Jean <br>
Mot de passe : Mklsdfee65e

