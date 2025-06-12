import os
import logging
from flask_cors import CORS
from flask import Flask, send_from_directory, jsonify
from werkzeug.utils import safe_join
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import DevelopmentConfig  # Ou ProductionConfig selon l'environnement
from flask_restx import Api  # Swagger intégré
# Déclarez db en dehors de la fonction create_app
db = SQLAlchemy()
migrate = Migrate()
logging.basicConfig(level=logging.INFO)  # Pour afficher les logs dans la console

# Initialisation de l'API Swagger
api = Api(
    title='API de Mon Application',
    version='1.0',
    description='Documentation Swagger de l\'API',
    doc='/docs'  # Swagger UI accessible via /docs
)
def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(DevelopmentConfig)  # Applique la configuration

    db.init_app(app)
    migrate.init_app(app, db)
    # Définir l'emplacement du dossier de téléchargement
    app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploads')  # Le dossier de stockage des images

    @app.route('/uploads/<filename>')
    def uploaded_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    # Importation des Namespaces (au lieu des blueprints classiques)
    api.init_app(app)
    # Initialiser Swagger avec l'app
    from app.swagger.produit_route import produit_ns
    from app.swagger.panier_route import panier_ns
    from app.swagger.commande_route import commande_ns
    # Enregistrer les namespaces avec des préfixes
    api.add_namespace(produit_ns, path='/produits')
    api.add_namespace(panier_ns, path='/paniers')
    api.add_namespace(commande_ns, path='/commandes')

    # Importation des modèles après la création de l'app
    from app.routes.produit_route import produit_bp
    app.register_blueprint(produit_bp)
    from app.routes.panier_route import panier_bp
    app.register_blueprint(panier_bp)
    from app.routes.commande_route import commande_bp
    app.register_blueprint(commande_bp)
    
    return app  # Retourner l'application créée

