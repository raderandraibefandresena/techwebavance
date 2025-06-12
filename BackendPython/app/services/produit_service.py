import os
import logging
from werkzeug.utils import secure_filename
from flask import current_app 
from app import db
from app.models.produit import Produit

class ProduitService:
    @staticmethod
    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

    @staticmethod
    def save_image(file):
        if file and ProduitService.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            print(f"Image enregistrée à: {file_path}")
            file.save(file_path)
            return filename
        return None

    @staticmethod
    def ajout_produit(photo, nom, description, prix, quantite_disponible):
        try:
            # Validate prix and quantite_disponible
            try:
                prix = float(prix)
                quantite_disponible = int(quantite_disponible)
                if prix <= 0 or quantite_disponible <= 0:
                    return None  
            except ValueError:
                return None  

            # Save image if provided
            image_path = ProduitService.save_image(photo) if photo else None  # Correction ici
            
            # Create the product
            produit = Produit(
                photo=image_path, 
                nom=nom, 
                description=description, 
                prix=prix, 
                quantite_disponible=quantite_disponible
            )
            db.session.add(produit)
            db.session.commit()
            return produit
        except Exception as e:
            db.session.rollback()
            logging.error(f"Error while adding product: {e}")
            return None

    @staticmethod
    def liste_produits():
        return Produit.query.all()

    @staticmethod
    def liste_produit_by_id(produit_id):
        return Produit.query.get(produit_id)

    @staticmethod
    def modification_produit(produit_id, photo=None, nom=None, description=None, prix=None, quantite_disponible=None):
        produit = Produit.query.get(produit_id)
        if not produit:
            return None

        try:
            if photo:
                produit.photo = ProduitService.save_image(photo)  # Correction ici
            if nom:
                produit.nom = nom
            if description:
                produit.description = description
            if prix:
                produit.prix = float(prix)
            if quantite_disponible:
                produit.quantite_disponible = int(quantite_disponible)

            db.session.commit()
            return produit
        except Exception as e:
            db.session.rollback()
            print(f"Erreur lors de la mise à jour du produit : {e}")
            return None

    @staticmethod
    def suppression_produit(produit_id):
        produit = Produit.query.get(produit_id)
        if not produit:
            return False

        try:
            db.session.delete(produit)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Erreur lors de la suppression du produit : {e}")
            return False
