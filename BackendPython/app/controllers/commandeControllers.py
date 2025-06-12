from app.services.commande_service import CommandeService

@staticmethod
def commander():
    return CommandeService.commander_panier()
