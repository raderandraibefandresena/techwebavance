from datetime import datetime
from app import db
from app.models.commande import Commande
from app.models.panier import Panier
from app.models.produit import Produit

from app import db
from app.models.panier import Panier
from app.models.produit import Produit
from app.models.commande import Commande
from datetime import datetime

class CommandeService:
    @staticmethod
    def commander_panier():
        try:
            # Récupérer tous les articles du panier
            paniers = Panier.query.all()
            if not paniers:
                return {"message": "Le panier est vide"}, 400

            # Calculer le prix total et la quantité totale
            prix_total = sum(panier.prix_total for panier in paniers)
            quantite_total = sum(panier.quantite for panier in paniers)

            commandes = []

            for panier in paniers:
                # Ajouter chaque article du panier à la commande
                commande_item = Commande(
                    panier_id=panier.id,
                    nom_produit=panier.produit.nom if panier.produit else None,
                    description=panier.produit.description if panier.produit else None,
                    prix_produit=panier.produit.prix if panier.produit else 0,
                    prix_total_commande=panier.prix_total,
                    quantite_panier=panier.quantite,
                    quantite_commande=quantite_total,  # Total de toutes les quantités du panier
                    date_commande=datetime.utcnow(),
                    photo=panier.produit.photo if panier.produit else None
                )
                db.session.add(commande_item)
                commandes.append({
                    "produit_id": panier.produit.id if panier.produit else None,
                    "nom_produit": panier.produit.nom if panier.produit else None,
                    "description": panier.produit.description if panier.produit else None,
                    "photo": panier.produit.photo if panier.produit else None,
                    "quantite": panier.quantite,
                    "prix_total": panier.prix_total
                })

                # Supprimer l'article du panier après la commande
                db.session.delete(panier)

            db.session.commit()

            return {
                "message": "Commande passée avec succès", 
                "prix_total": prix_total, 
                "quantite_total": quantite_total, 
                "commandes": commandes
            }, 201
        except Exception as e:
            db.session.rollback()
            print(f"Erreur lors du passage de la commande : {e}")
            return {"error": "Erreur interne du serveur"}, 500
    @staticmethod
    def get_all_commandes():
        return Commande.query.all()
    @staticmethod
    def get_commande_by_id(commande_id):
        return Commande.query.get(commande_id)
    @staticmethod
    def update_commande(commande_id, nom=None, description=None, prix_total=None, quantite=None, photo=None):
        commande = Commande.query.get(commande_id)
        if not commande:
            print(f"⚠️ Commande non trouvée pour ID : {commande_id}")
            return None  # Retourner None si la commande n'existe pas

        try:
            # Mettre à jour chaque champ seulement si la valeur est non nulle
            if nom:
                commande.nom = nom
            if description:
                commande.description = description
            if prix_total:
                commande.prix_total_commande = prix_total
            if quantite:
                commande.quantite_commande = quantite
            if photo:
                commande.photo = photo

            db.session.commit()
            return commande  # Retourner la commande mise à jour

        except Exception as e:
            db.session.rollback()
            print(f" Erreur lors de la mise à jour de la commande : {e}")
            return None  # Retourner None en cas d'erreur
    @staticmethod
    def delete_commande(commande_id):
        commande = Commande.query.get(commande_id)
        if not commande:
            return False  # Commande non trouvée

        try:
            db.session.delete(commande)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Erreur lors de la suppression de la commande : {e}")
            return False
