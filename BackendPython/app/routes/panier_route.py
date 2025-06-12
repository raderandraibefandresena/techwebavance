from flask import Blueprint
from app.controllers.panierControllers import AjoutPanier, ListePanier, ModificationPanier, SuppressionPanier
panier_bp = Blueprint('panier_bp', __name__)

panier_bp.add_url_rule('/ajoutPanier', 'AjoutPanier', AjoutPanier, methods=['POST'])
panier_bp.add_url_rule('/listePanier', 'ListePanier', ListePanier, methods=['GET'])
panier_bp.add_url_rule('/modificationPanier/<int:panier_id>', 'ModificationPanier', ModificationPanier, methods=['PUT'])
panier_bp.add_url_rule('/suppressionPanier/<int:panier_id>', 'SuppressionPanier', SuppressionPanier, methods=['DELETE'])
