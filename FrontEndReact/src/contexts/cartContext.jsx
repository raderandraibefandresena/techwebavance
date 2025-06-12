// contexts/cartContext.js
import React, { createContext, useState } from 'react';

export const CartContext = createContext();

export const CartProvider = ({ children }) => {
  const [cartItems, setCartItems] = useState([]);

  const addToCart = (product) => {
    setCartItems(prevItems => {
      const existingItem = prevItems.find(item => item.id === product.id);
      if (existingItem) {
        
        const newQuantity = Math.min(
          existingItem.quantity + product.quantity,
          product.quantite_disponible || Infinity
        );
        return prevItems.map(item =>
          item.id === product.id ? { ...item, quantity: newQuantity } : item
        );
      }
      
      return [...prevItems, { ...product, quantity: Math.min(product.quantity, product.quantite_disponible || Infinity) }];
    });
  };

  const updateQuantity = (id, newQuantity) => {
    setCartItems(prevItems =>
      prevItems.map(item => {
        if (item.id === id) {
          const quantity = Math.min(newQuantity, item.quantite_disponible || Infinity);
          return { ...item, quantity: quantity > 0 ? quantity : 1 };
        }
        return item;
      })
    );
  };

  const removeItem = (id) => {
    setCartItems(prevItems => prevItems.filter(item => item.id !== id));
  };

  const clearCart = () => setCartItems([]);

  return (
    <CartContext.Provider value={{ cartItems, addToCart, updateQuantity, removeItem, clearCart }}>
      {children}
    </CartContext.Provider>
  );
};
