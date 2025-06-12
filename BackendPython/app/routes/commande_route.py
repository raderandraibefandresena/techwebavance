from flask import Blueprint
from app.controllers.commandeControllers import commander


commande_bp = Blueprint('commande_bp', __name__) 

commande_bp.add_url_rule('/ajoutCommande', 'commander', commander, methods=['POST']) # ajout des articles

# commande_bp.add_url_rule('/listes', 'listeArticle', listeArticle, methods=['GET']) # liste des articles