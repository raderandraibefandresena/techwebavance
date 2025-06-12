from flask_restx import Namespace, Resource, fields
from app.controllers.produitControllers import AjoutProduit, listeProduit, modificationProduit, suppressionProduit

produit_ns = Namespace('produits', description='Gestion des produits')

produit_model = produit_ns.model('Produit', {
    'nom': fields.String(required=True, description='Nom du produit'),
    'description': fields.String(description='Description du produit'),
    'prix': fields.Float(required=True, description='Prix du produit'),
    'quantite_disponible': fields.Integer(required=True, description='Quantité disponible'),
    'photo': fields.String(description='URL ou chemin de la photo'),
})

@produit_ns.route('/ajoutProduit')
class AjoutProduitResource(Resource):
    @produit_ns.expect(produit_model)
    def post(self):
        return AjoutProduit()

@produit_ns.route('/listeProduit')
class ListeProduitResource(Resource):
    def get(self):
        return listeProduit()

@produit_ns.route('/modificationProduit/<int:produit_id>')
class ModificationProduitResource(Resource):
    @produit_ns.expect(produit_model)
    def put(self, produit_id):
        return modificationProduit(produit_id)

@produit_ns.route('/suppressionProduit/<int:produit_id>')
class SuppressionProduitResource(Resource):
    def delete(self, produit_id):
        return suppressionProduit(produit_id)
