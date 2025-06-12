from flask_restx import Namespace, Resource, fields
from app.controllers.commandeControllers import commander

commande_ns = Namespace('commandes', description='Gestion des commandes')

commande_model = commande_ns.model('Commande', {
    'panier_id': fields.Integer(required=True, description='ID du panier'),
    # autres champs
})


@commande_ns.route('/ajoutCommande')
class CommandeResource(Resource):
    @commande_ns.expect(commande_model)
    def post(self):
        return commander()
