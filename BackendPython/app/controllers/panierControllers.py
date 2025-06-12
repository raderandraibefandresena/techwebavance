from flask import Blueprint, request, jsonify
from app import db
from sqlalchemy import func
from app.models.panier import Panier
from app.models.produit import Produit
from app.services.panier_service import PanierService

@staticmethod
def AjoutPanier():
    data = request.get_json()
    produit_id = data.get('produit_id')
    quantite = data.get('quantite')
    if not produit_id or not quantite:
        return jsonify({'error': 'Données incomplètes'}), 400

    panier = PanierService.ajout_panier(produit_id, int(quantite))
    
    if panier:
        paniers_list = Panier.query.all()
        prix_total = sum(p.prix_total for p in paniers_list)
        quantite_total = sum(p.quantite for p in paniers_list)
        paniers_data = []
        for panier_item in paniers_list:
            produit = Produit.query.get(panier_item.produit_id)
            paniers_data.append({
                'produit_id': panier_item.produit_id,
                'nom_produit': produit.nom,
                "photo": f"{request.host_url}uploads/{produit.photo}" if produit.photo else None,
                'quantite': panier_item.quantite,
                'prix_total': panier_item.prix_total
            })

        return jsonify({
            'message': 'Produit ajouté au panier avec succès',
            'panier_id': panier.id,
            'prix_total': prix_total,
            'quantite_total': quantite_total,
            'panier': paniers_data
        }), 201

    return jsonify({'error': 'Erreur lors de l\'ajout au panier'}), 500

@staticmethod
def ListePanier():
    try:
        # Récupérer tous les paniers
        paniers = Panier.query.all()
        
        if paniers:
            # Calculer la somme du prix total et de la quantité totale dans le panier
            prix_total = sum(panier.prix_total for panier in paniers)
            quantite_total = sum(panier.quantite for panier in paniers)

            # Créer la réponse avec les détails des paniers
            paniers_data = [
                {
                    "produit_id": panier.produit_id,
                    "nom_produit": panier.produit.nom if panier.produit else None,
                    "photo": f"{request.host_url}uploads/{panier.produit.photo}" if panier.produit and panier.produit.photo else None,
                    "quantite": panier.quantite,
                    "prix_total": panier.prix_total,
                    'description': panier.produit.description if panier.produit else None,
                }
                for panier in paniers
            ]
            
            # Renvoyer les informations complètes avec la somme totale
            return jsonify({
                "message": "Panier récupéré avec succès",
                "panier": paniers_data,
                "prix_total": prix_total,
                "quantite_total": quantite_total
            }), 200
        else:
            return jsonify({"message": "Panier vide"}), 404
    except Exception as e:
        print(f"Erreur lors de la récupération des paniers : {e}")
        return jsonify({"error": "Erreur interne du serveur"}), 500

# Route pour obtenir un panier par ID
@staticmethod
def get_panier(panier_id):
    panier = PanierService.get_panier_by_id(panier_id)
    if panier:
        return jsonify({
            'id': panier.id,
            'produit': panier.produit.nom if panier.produit else None,
            'quantite': panier.quantite,
            'date_creation': panier.date_creation.strftime('%Y-%m-%d %H:%M:%S')
        }), 200
    return jsonify({'error': 'Panier non trouvé'}), 404

# mettre à jour la quantité d'un produit dans le panier
@staticmethod
def ModificationPanier(panier_id):
    data = request.get_json()
    quantite = data.get('quantite')

    panier = PanierService.modification_panier(panier_id, quantite)
    if panier:
        return jsonify({"message": "Panier mis à jour avec succès!"}), 200
    return jsonify({'error': 'Erreur lors de la mise à jour du panier'}), 500

#suppression d'un produit du panier
@staticmethod
def SuppressionPanier(panier_id):
    if PanierService.suppression_panier(panier_id):
        return jsonify({"message": "Produit supprimé du panier avec succès!"}), 200
    return jsonify({'error': 'Erreur lors de la suppression du panier'}), 500
