import React, { useContext } from 'react';
import { CartContext } from '../contexts/cartContext';
import { toast } from 'react-toastify'; 
import '../css/cart.css';

const Cart = () => {
  const { cartItems, updateQuantity, removeItem, clearCart } = useContext(CartContext);

  const subtotal = cartItems.reduce((total, item) => total + item.price * item.quantity, 0);
  const tax = subtotal * 0.06;
  const shipping = 20.0;
  const discount = 6.0;
  const total = subtotal + tax + shipping - discount;

  const handleIncrease = (itemId, currentQuantity) => updateQuantity(itemId, currentQuantity + 1);
  const handleDecrease = (itemId, currentQuantity) => currentQuantity > 1 && updateQuantity(itemId, currentQuantity - 1);
  const handleRemove = (itemId) => removeItem(itemId);

  const handleCheckout = () => {
    clearCart();
    toast.success('Achat validé ! Merci pour votre commande.', {
      position: "top-center",
      autoClose: 5000,
    });
  };

  return (
    <div className="cart-container">
      <h2>Your Bag</h2>

      <div className="cart-layout">
        <div className="cart-items">
          {cartItems.map((item, index) => (
            <React.Fragment key={item.id}>
              <div className="cart-item">
                <img src={item.images[0]} alt={item.name} className="item-image" />
                <div className="item-details">
                  <div className="item-h3p">
                    <h3>{item.brand}</h3>
                    <p>${item.price.toFixed(2)}</p>
                  </div>
                  <p>{item.name}</p>
                  <div className="item-quantity">
                    <button onClick={() => handleDecrease(item.id, item.quantity)}>-</button>
                    <span>{item.quantity}</span>
                    <button onClick={() => handleIncrease(item.id, item.quantity)}>+</button>
                    <button className="remove-button" onClick={() => handleRemove(item.id)}>
                      <u>Remove</u>
                    </button>
                  </div>
                </div>
              </div>
              {index < cartItems.length - 1 && <hr />}
            </React.Fragment>
          ))}
        </div>

        <div className="summary">
          <h2>Summary</h2>
          <div className="summary-details">
            <p>Subtotal <span>${subtotal.toFixed(2)}</span></p>
            <p>Shipping and delivery <span>${shipping.toFixed(2)}</span></p>
            <p>Tax <span>${tax.toFixed(2)}</span></p>
            <p>Discount <span style={{ color: 'red' }}>-${discount.toFixed(2)}</span></p>
          </div>
          <div className="total">
            <h3>Total</h3>
            <p>${total.toFixed(2)}</p>
          </div>
          <button className="checkout-button" onClick={handleCheckout}>
            Checkout →
          </button>
        </div>
      </div>
    </div>
  );
};

export default Cart;
