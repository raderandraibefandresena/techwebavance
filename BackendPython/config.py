import os
from dotenv import load_dotenv

load_dotenv()  # Charger les variables d'environnement à partir du fichier .env

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads') # Dossier où stocker les images
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

class Config:
    """Configuration de base pour l'application Flask"""
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:246822@localhost:5432/e_commerce')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'clé_secrète')

class DevelopmentConfig(Config):
    """Configuration spécifique pour le développement"""
    DEBUG = True

class ProductionConfig(Config):
    """Configuration spécifique pour la production"""
    DEBUG = False
