from flask import Blueprint, request, jsonify, current_app
from app import db
from app.models.produit import Produit
from app.services.produit_service import ProduitService

# Ajout d'un produit
@staticmethod
def AjoutProduit():
    if 'photo' not in request.files:
        return jsonify({'error': 'Aucune image fournie'}), 400
    photo = request.files['photo']
    nom = request.form.get('nom')
    description = request.form.get('description')
    prix = request.form.get('prix')
    quantite_disponible = request.form.get('quantite_disponible')

    if not nom or not prix or not quantite_disponible:
        return jsonify({'error': 'Données incomplètes'}), 400

    produit = ProduitService.ajout_produit(photo, nom, description, prix, quantite_disponible)

    if produit:
        return jsonify({'message': 'Produit ajouté avec succès', 'produit_id': produit.id}), 201
    return jsonify({'error': 'Erreur lors de l\'ajout du produit'}), 500

# Obtenir tous les produits
@staticmethod
def listeProduit():
        try:
            # Fetch the list of products
            produits = ProduitService.liste_produits()

            # If there are products, return them in a JSON response
            if produits:
                return jsonify([
                    {
                        "id": produit.id,
                        "photo": f"{request.host_url}uploads/{produit.photo}" if produit.photo else None,
                        "nom": produit.nom,
                        "description": produit.description,
                        "prix": produit.prix,
                        "quantite_disponible": produit.quantite_disponible
                    }
                    for produit in produits
                ]), 200

            # If no products found, return a 404 with a message
            return jsonify({"message": "Aucun produit trouvé"}), 404

        except Exception as e:
            # In case of an error, return a 500 status code and log the error
            print(f"Error fetching products: {e}")
            return jsonify({"message": "Erreur interne du serveur"}), 500   
# Obtenir un produit par ID
@staticmethod
def get_produit(produit_id):
    produit = ProduitService.liste_produit_by_id(produit_id)
    if produit:
        return jsonify({
            'id': produit.id,
            'nom': produit.nom,
            'description': produit.description,
            'prix': produit.prix,
            'quantite_disponible': produit.quantite_disponible,
            "photo": f"{request.host_url}uploads/{produit.photo}" if produit.photo else None,
        }), 200
    return jsonify({'error': 'Produit non trouvé'}), 404

# Mettre à jour un produit
@staticmethod
def modificationProduit(produit_id):
    data = request.form
    photo = request.files.get('photo')

    produit = ProduitService.modification_produit(produit_id, photo, data.get('nom'), data.get('description'), data.get('prix'), data.get('quantite_disponible'))
    if produit:
        return jsonify({"message": "Produit mis à jour avec succès!"}), 200
    return jsonify({'error': 'Erreur lors de la mise à jour du produit'}), 500

# Suppression d'un produit
@staticmethod
def suppressionProduit(produit_id):
    if ProduitService.suppression_produit(produit_id):
        return jsonify({"message": "Produit supprimé avec succès!"}), 200
    return jsonify({'error': 'Erreur lors de la suppression du produit'}), 500
