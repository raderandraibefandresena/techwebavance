from app import db
from app.models.panier import Panier
from app.models.produit import Produit
from datetime import datetime

class PanierService:
    @staticmethod
    def ajout_panier(produit_id, quantite):
        try:
            # Récupérer le produit
            produit = Produit.query.get(produit_id)
            if not produit:
                return None  # Le produit n'existe pas

            # Vérifier si suffisamment de stock est disponible
            if produit.quantite_disponible < quantite:
                return None  # Pas assez de stock disponible
            
            # Calculer le prix total pour le produit ajouté au panier
            prix_total = produit.prix * quantite
            
            # Vérifier si le produit est déjà dans le panier
            panier_existant = Panier.query.filter_by(produit_id=produit_id).first()
            if panier_existant:
                # Si le produit est déjà dans le panier, augmenter la quantité
                if produit.quantite_disponible >= quantite:
                    panier_existant.quantite += quantite
                    panier_existant.prix_total += prix_total  # Ajouter au prix total existant
                    produit.quantite_disponible -= quantite  # Réduire le stock
                    db.session.commit()  # Sauvegarder les changements
                    return panier_existant
                else:
                    return None  # Pas assez de stock pour augmenter la quantité
            else:
                # Si le produit n'est pas dans le panier, ajouter un nouvel enregistrement
                panier = Panier(produit_id=produit_id, quantite=quantite)
                panier.prix_total = prix_total  # Assigner le prix total calculé ici
                produit.quantite_disponible -= quantite  # Réduire le stock
                db.session.add(panier)
                db.session.commit()  # Sauvegarder les changements
                return panier
        except Exception as e:
            db.session.rollback()
            print(f"Erreur lors de l'ajout au panier : {e}")
            return None
    @staticmethod
    def liste_paniers():
        return Panier.query.all()
    @staticmethod
    def get_panier_by_id(panier_id):
        return Panier.query.get(panier_id)
    @staticmethod
    def modification_panier(panier_id, quantite=None):
        panier = Panier.query.get(panier_id)
        if not panier:
            return None  # Panier introuvable

        try:
            produit = panier.produit  # Récupérer le produit lié à cet élément du panier
            old_quantite = panier.quantite  # Stocker l'ancienne quantité dans le panier

            if quantite is not None:
                # Vérifier si la quantité change
                if quantite > old_quantite:  # Si la quantité dans le panier augmente
                    if produit.quantite_disponible >= quantite - old_quantite:
                        produit.quantite_disponible -= (quantite - old_quantite)  # Réduire le stock du produit
                    else:
                        return None  # Pas assez de stock disponible
                elif quantite < old_quantite:  # Si la quantité dans le panier diminue
                    produit.quantite_disponible += (old_quantite - quantite)  # Augmenter le stock du produit

                # Mettre à jour la quantité dans le panier
                panier.quantite = quantite
                db.session.commit()  # Enregistrer les changements dans la base de données

            return panier
        except Exception as e:
            db.session.rollback()
            print(f"Erreur lors de la mise à jour du panier : {e}")
            return None  # Retourner None en cas d'erreur
    @staticmethod
    def suppression_panier(panier_id):
        panier = Panier.query.get(panier_id)
        if not panier:
            return False  # Cart not found

        try:
            produit = panier.produit  # Get the product related to the cart item
            produit.quantite_disponible += panier.quantite  # Revert the quantity decrease
            db.session.commit()  # Commit the product quantity update

            db.session.delete(panier)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error removing product from cart: {e}")
            return False
