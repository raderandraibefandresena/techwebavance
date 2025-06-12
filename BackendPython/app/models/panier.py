from app import db
from datetime import datetime

class Panier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    produit_id = db.Column(db.Integer, db.ForeignKey('produit.id'), nullable=False)
    quantite = db.Column(db.Integer, nullable=False)
    prix_total = db.Column(db.Float, nullable=False)  # Prix total du produit
    date_creation = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    # Relation avec Produit
    produit = db.relationship('Produit', backref=db.backref('paniers', lazy=True))

    def __init__(self, produit_id, quantite, date_creation=None):
        # Le constructeur ne prend plus prix_total, il est calculé ailleurs
        self.produit_id = produit_id
        self.quantite = quantite
        self.date_creation = date_creation or datetime.utcnow()
        # Pas besoin de définir prix_total ici, il sera calculé dans create_panier
