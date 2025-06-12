
//activation sur windows
venv\Scripts\activate
pip install flask    
pip freeze > requirements.txt  
pip install -r requirements.txt
//structure mvc
pip install flask flask-sqlalchemy
pip install flask-cors
//installation dotenv
pip install  python-dotenv
(.env)
//installation migration 
pip install flask-migrate
//voir la historique 
flask db history
//qui est un connecteur PostgreSQL pour Python, n'est pas installé dans ton environnement virtuel.
pip install psycopg2
//La commande flask db stamp head marquera la base de données comme étant à jour avec la dernière migration
flask db stamp head
//modification
flask db upgrade
//migrate db
flask db init
//Cela génère un fichier de migration basé sur les modèles.
flask db migrate -m "Initial migration"
flask db migrate -m "Ajout de la colonne date_abonnement à la table abonnements"

Commande	Description
flask db init	Initialise le système de migrations (à faire une seule fois).
flask db migrate -m "Message"	Crée un fichier de migration basé sur les modèles.
flask db upgrade	Applique les migrations à la base de données.
flask db downgrade	Annule la dernière migration.
flask db history	Liste l'historique des migrations.

//lancement python flask
flask run

//installation swagger 
pip install flasgger
pip install flask-restx


New-Item -ItemType Directory -Path "app\models"
New-Item -ItemType Directory -Path "app\views"
New-Item -ItemType Directory -Path "app\controllers"
New-Item -ItemType Directory -Path "app\forms"
