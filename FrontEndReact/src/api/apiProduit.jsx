import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL;

// Récupérer la liste des produits
 
export const getProduits = async () => {
  try {
    const response = await axios.get(`${API_URL}/listeProduit`);
    console.log("API Response:", response.data); // Debug
    return response.data;
  } catch (error) {
    console.error("Erreur API:", error.response?.data || error.message);
    return null;
  }
};

//  Ajouter un nouveau produit

export const ajouterProduit = async (data) => {
  try {
    const response = await axios.post(`${API_URL}/ajoutProduit`, data);
    return response.data;
  } catch (error) {
    console.error("Erreur lors de l'ajout du produit:", error);
    return null;
  }
};

//  Modification un produit

export const modificationProduit = async (data) => {
    try {
      const response = await axios.post(`${API_URL}/modificationProduit/${id}`, data);
      return response.data;
    } catch (error) {
      console.error("Erreur lors de modification du produit:", error);
      return null;
    }
  };

//  Supprimer un produit

export const supprimerProduit = async (id) => {
  try {
    const response = await axios.delete(`${API_URL}/supprimerProduit/${id}`);
    return response.data;
  } catch (error) {
    console.error("Erreur lors de la suppression du produit:", error);
    return null;
  }
};
