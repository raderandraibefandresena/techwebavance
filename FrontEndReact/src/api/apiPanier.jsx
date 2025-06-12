import axios from "axios";
const API_URL = import.meta.env.VITE_API_URL;

export const ajoutPanier = async(data) => {
    try {
        const response = await axios.post(`${API_URL}/ajoutPanier`, data);
        return response.data;
    } catch (error) {
        console.error(error.response?.data || error.message);
        throw error;
    }
}
 
export const modificationPanier = async (data) => {
    try {
      const response = await axios.post(`${API_URL}/modificationPanier/${id}`, data);
      return response.data;
    } catch (error) {
      console.error("Erreur lors de modification du panier:", error);
      return null;
    }
  };
export const afficherPanier = async() => {
    try {
        const response = await axios.get(`${API_URL}/listePanier`);
        return response.data;
    } catch (error) {
        return res.status(500).json(error);
    }
}
export const suppressionPanier = async(id)=>{
    try {
        const response = await axios.delete(`${API_URL}/suppressionPanier/${id}`);
        return response.data;
    } catch (error) {
        return res.status(),json(error,"erreur lors de suppression");
    }
}


