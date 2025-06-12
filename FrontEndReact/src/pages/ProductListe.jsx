import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import Image2 from '/image/Image2.png';
import '../css/productListe.css';
import { getProduits } from "../api/apiProduit";

const ProductList = () => {
  const [produits, setProduits] = useState([]);
  const [loading, setLoading] = useState(true); 
  const [error, setError] = useState(null); 

  useEffect(() => {
    fetchProduits();
  }, []);

  const fetchProduits = async () => {
    try {
      const data = await getProduits();
      if (data) {
        setProduits(data);
      } 
    } catch (error) {
      setError('Failed to load products');
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <div className="container">
        <div className="text-container">
          <h1 style={{ margin: '10px 0', fontSize: 'clamp(24px, 10vw, 60px)' }}>
            <span style={{ color: 'rgb(184, 62, 13)' }}>25% OFF</span>
          </h1>
          <h1 style={{ margin: '10px 0 0 0', fontSize: 'clamp(35px, 4.5vw, 60px)' }}>
            Summer Sale
          </h1>
          <p style={{ margin: '40px 0', fontSize: 'clamp(12px, 3vw, 21px)', color: '#555' }}>
            Discover our summer styles with discount
          </p>
          <button className="button">Shop Now →</button>
        </div>
        <img className="image" src="image/Image1.png" alt="Promo Image" />
      </div>

      {/* Product Section */}
      <div className="product-section">
  <h2>Explore our latest drops</h2>
  <div className="product">
    {produits.map((produit) => (
      <Link to={`/product/${produit.id}`} key={produit.id} className="product-link">
        <div className="product-list">
          <div className="image-container">
            <img 
              src={produit.photo || Image2} 
              alt={produit.nom}
              onError={(e) => e.target.src = Image2}
            />
          </div>
          <h3>{produit.nom}</h3>
          <p className="description">{produit.description}</p>
          <p className="price">${produit.prix.toFixed(2)}</p>
        </div>
      </Link>
    ))}
  </div>
</div>
    </>
  );
};

export default ProductList;
