import React, { useState, useEffect, useContext } from 'react';
import { useParams } from 'react-router-dom';
import { CartContext } from '../contexts/cartContext';
import '../css/product.css';
import { toast } from 'react-toastify'; 
import { getProduitById } from '../api/apiProduit';
import { ajoutPanier } from '../api/apiPanier';

const Product = () => {
  const { id } = useParams();
  const [product, setProduct] = useState(null);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [quantity, setQuantity] = useState(1);
  const { addToCart } = useContext(CartContext);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchProduct = async () => {
      try {
        const data = await getProduitById(id);
        if (data) {
          const images = Array.isArray(data.images)
            ? data.images
            : data.images
            ? [data.images]
            : data.photo
            ? [data.photo]
            : ["/image/Image2.png"];

          setProduct({ ...data, images });
        } else {
          setError('Produit non trouvé.');
        }
      } catch (err) {
        setError('Échec du chargement du produit.');
      } finally {
        setLoading(false);
      }
    };
    fetchProduct();
  }, [id]);

  const handleNextImage = () => {
    if (product) {
      setCurrentIndex((prevIndex) => (prevIndex + 1) % product.images.length);
    }
  };

  const handlePrevImage = () => {
    if (product) {
      setCurrentIndex((prevIndex) =>
        prevIndex === 0 ? product.images.length - 1 : prevIndex - 1
      );
    }
  };

  const handleIncrease = () => setQuantity((prev) => prev + 1);
  const handleDecrease = () => quantity > 1 && setQuantity((prev) => prev - 1);

  const handleAddToCart = async () => {
    try {
      const data = { produit_id: product.id, quantite: quantity };
      await ajoutPanier(data);

      addToCart({
        id: product.id,
        name: product.nom || product.name,
        price: parseFloat(product.prix),       // ✅ Price tokony ho float
        quantity: parseInt(quantity, 10),      // ✅ Quantity ho integer
        images: product.images,
        brand: product.brand,
      });

      toast.success("Produit ajouté au panier !");
    } catch (error) {
      console.error("Erreur ajout panier:", error);
      toast.error("Erreur lors de l'ajout au panier !");
    }
  };

  if (loading) return <div>Chargement...</div>;
  if (error) return <div>{error}</div>;
  if (!product) return <div>Produit non trouvé.</div>;

  return (
    <div className="product-container">
      <div className="main-section">
        <div className="image-section">
          <img
            src={product.images[currentIndex]}
            alt={product.nom || product.name}
            className="product-image"
            onError={(e) => (e.target.src = "/image/Image2.png")}
          />
          <div className="navigation-buttons">
            <button className="nav-button" onClick={handlePrevImage}>&#10094;</button>
            <div className="pagination">
              {product.images.map((_, index) => (
                <span
                  key={index}
                  className={`dot ${index === currentIndex ? "active" : ""}`}
                  onClick={() => setCurrentIndex(index)}
                ></span>
              ))}
            </div>
            <button className="nav-button" onClick={handleNextImage}>&#10095;</button>
          </div>
        </div>

        <div className="details-section">
          {product.brand && <h1 className="product-brand">{product.brand}</h1>}
          <h2 className="product-name">{product.nom || product.name}</h2>
          <p className="product-price">${parseFloat(product.prix).toFixed(2)}</p>
          <hr className="divider" />

          <div className="quantity-section">
            <p>Quantity</p>
            <div className="quantity-buttons">
              <button className="quantity-button" onClick={handleDecrease}>-</button>
              <span className="quantity-value">{quantity}</span>
              <button className="quantity-button" onClick={handleIncrease}>+</button>
            </div>
          </div>

          <button className="add-to-cart-button" onClick={handleAddToCart}>
            Add to Cart
          </button>
        </div>
      </div>

      <div className="description-section">
        <div className="text-section">
          <h2>Description</h2>
          <hr className="ligne" />
          <p>
            Energize your look with a fresh take on heritage adidas style. The
            adidas Daily 3.0 Shoes cut a classic profile with a modern suede
            upper. Your walk across campus or commute across town has never
            looked or felt this good.
          </p>
          <ul>
            <li>Regular fit</li>
            <li>Lace closure</li>
            <li>Rubber outsole with vulcanized look</li>
            <li>Imported</li>
          </ul>
        </div>

        <div className="description-image-section">
          <img src="/image/Image6.png" alt="Description Image" className="description-image" />
        </div>
      </div>
    </div>
  );
};

export default Product;
