import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL;

/**
 * Récupérer la liste des produits
 */
export const getProduits = async () => {
  try {
    const response = await axios.get(`${API_URL}/listeProduit`);
    return response.data;
  } catch (error) {
    console.error("Erreur API:", error.response?.data || error.message);
    return null;
  }
};

/**
 * Ajouter un nouveau produit (multipart/form-data)
 */
export const ajouterProduit = async (data) => {
  try {
    const response = await axios.post(`${API_URL}/ajoutProduit`, data, {
      headers: { "Content-Type": "multipart/form-data" },
    });
    return response.data;
  } catch (error) {
    console.error("Erreur lors de l'ajout du produit:", error.response?.data || error.message);
    return null;
  }
};

/**
 * Modifier un produit
 * @param {number} id - ID du produit à modifier
 * @param {FormData} data - Données du produit (FormData pour inclure photo si besoin)
 */
export const modificationProduit = async (id, data) => {
  try {
    const response = await axios.put(`${API_URL}/modificationProduit/${id}`, data, {
      headers: { "Content-Type": "multipart/form-data" },
    });
    return response.data;
  } catch (error) {
    console.error("Erreur lors de la modification du produit:", error.response?.data || error.message);
    return null;
  }
};

/**
 * Supprimer un produit
 * @param {number} id - ID du produit
 */
export const supprimerProduit = async (id) => {
  try {
    const response = await axios.delete(`${API_URL}/suppressionProduit/${id}`);
    return response.data;
  } catch (error) {
    console.error("Erreur lors de la suppression du produit:", error.response?.data || error.message);
    return null;
  }
};

/**
 * Obtenir un produit par ID
 * @param {number} id
 */
export const getProduitById = async (id) => {
  try {
    const response = await axios.get(`${API_URL}/produits/${id}`);
    return response.data;
  } catch (error) {
    console.error("Erreur lors de la récupération du produit:", error.response?.data || error.message);
    return null;
  }
};
