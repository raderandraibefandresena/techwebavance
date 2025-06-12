from app import db

class Produit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    prix = db.Column(db.Float, nullable=False)
    quantite_disponible = db.Column(db.Integer, nullable=False)
    photo = db.Column(db.String(255), nullable=True) 
    
    def __init__(self,nom,description,prix,quantite_disponible,photo):
        self.nom = nom
        self.description = description
        self.prix = prix
        self.quantite_disponible = quantite_disponible
        self.photo = photo