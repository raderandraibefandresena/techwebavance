import axios from "axios";
const API_URL =import.meta.env.VITA_API_URL;

export const ajoutCommande = async(data)=>{
    try {
        const response = await axios.post(`${API_URL}/ajoutCommande`,data);
        return response.data;
    } catch (error) {
        return res.status.json(error,"erreur d'ajout commande");
    }
}
