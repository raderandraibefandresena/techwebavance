from app import db
from datetime import datetime

class Commande(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    panier_id = db.Column(db.Integer,nullable=True)
    nom_produit = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    prix_produit = db.Column(db.Integer, nullable=False) 
    prix_total_commande = db.Column(db.Float, nullable=False)
    quantite_panier = db.Column(db.Integer, nullable=False) 
    quantite_commande = db.Column(db.Integer, nullable=False)
    date_commande = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    photo = db.Column(db.String(255))

    def __init__(self,panier_id,nom_produit,description,prix_produit,prix_total_commande,quantite_panier,quantite_commande,date_commande,photo):
        self.panier_id = panier_id
        self.nom_produit = nom_produit
        self.description = description
        self.prix_produit = prix_produit
        self.prix_total_commande = prix_total_commande
        self.quantite_panier = quantite_panier
        self.quantite_commande = quantite_commande
        self.date_commande = date_commande
        self.photo = photo
        
