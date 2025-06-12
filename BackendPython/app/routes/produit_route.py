from flask import Blueprint
from app.controllers.produitControllers import AjoutProduit, listeProduit, modificationProduit, suppressionProduit, get_produit


produit_bp = Blueprint('produit_bp', __name__) 

produit_bp.add_url_rule('/ajoutProduit', 'AjoutProduit', AjoutProduit, methods=['POST']) # ajout des articles

produit_bp.add_url_rule('/listeProduit', 'listeProduit', listeProduit, methods=['GET'])# liste des articles
produit_bp.add_url_rule('/produits/<int:produit_id>', 'get_produit', get_produit, methods=['GET'])
produit_bp.add_url_rule('/produits/<int:produit_id>', 'get_produit', get_produit, methods=['GET'])


#liste obtenir la liste un panier
produit_bp.add_url_rule('/modificationProduit/<int:produit_id>', 'modificationProduit', modificationProduit, methods=['PUT']) 
produit_bp.add_url_rule('/suppressionProduit/<int:produit_id>', 'suppressionProduit', suppressionProduit, methods=['DELETE']) 
