from flask_restx import Namespace, Resource, fields
from app.controllers.panierControllers import AjoutPanier, ListePanier, ModificationPanier, SuppressionPanier

panier_ns = Namespace('paniers', description='Gestion des paniers')

panier_model = panier_ns.model('Panier', {
    'produit_id': fields.Integer(required=True, description='ID du produit'),
    'quantite': fields.Integer(required=True, description='Quantité'),
    # autres champs si nécessaire
})


@panier_ns.route('/ajoutPanier')
class AjoutPanierResource(Resource):
    @panier_ns.expect(panier_model)
    def post(self):
        return AjoutPanier()


@panier_ns.route('/listePanier')
class ListePanierResource(Resource):
    def get(self):
        return ListePanier()


@panier_ns.route('/modificationPanier/<int:panier_id>')
class ModificationPanierResource(Resource):
    def put(self, panier_id):
        return ModificationPanier(panier_id)


@panier_ns.route('/suppresionPanier/<int:panier_id>')
class SuppresionPanierResource(Resource):
    def delete(self, panier_id):
        return SuppressionPanier(panier_id)
