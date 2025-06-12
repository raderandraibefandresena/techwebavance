// App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import ProductTable from './pages/ProductListe';
import Footer from './components/Footer';
import Product from './pages/Product';
import Cart from './pages/cart';
import { CartProvider } from './contexts/cartContext'; 
import './App.css';
import { ToastContainer } from 'react-toastify'; 
import 'react-toastify/dist/ReactToastify.css';

function App() {
  return (
    <CartProvider> 
      <Router>
        <Header />
        <main className="main-content">
          <Routes>
            <Route path="/carte" element={<Cart />} />
            <Route path="/" element={<ProductTable />} />
            <Route path="/product/:id" element={<Product />} />
          </Routes>
        </main>
        <Footer />
        <ToastContainer />
      </Router>
    </CartProvider>
  );
}

export default App;