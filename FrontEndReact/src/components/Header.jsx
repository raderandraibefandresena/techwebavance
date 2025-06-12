import React, { useContext } from 'react'; // Ampio ny useContext
import { useNavigate } from 'react-router-dom'; 
import { CartContext } from '../contexts/cartContext'; // Import CartContext

const Header = () => {
  const navigate = useNavigate();
  const { cartItems } = useContext(CartContext); // Mampiasa ny useContext

  // Kajio ny totalin'ny articles ao amin'ny cart
  const totalItems = cartItems.reduce((total, item) => total + item.quantity, 0);

  return (
    <div style={{ 
      display: 'flex', 
      justifyContent: 'space-between', 
      alignItems: 'center', 
      padding: '9px', 
      backgroundColor: '#fff',
      fontSize: 'clamp(16px, 4vw, 24px)', 
      borderBottom:'1px solid black'
    }}>
      {/* Titre SUN CO. aligné à gauche avec espacement dynamique */}
      <div style={{ 
        display: 'flex', 
        alignItems: 'center', 
        gap: '8px', /* ✅ Elanelana kely eo amin'ny sary sy ny soratra */
        margin: '0 0 0 clamp(20px, 10vw, 160px)',
        whiteSpace: 'nowrap' /* ✅ Mba tsy hisaraka amin'ny écran kely */
      }}> 
        <img 
          src="image/Image8.png" 
          alt="Promo Image" 
          style={{
            width: 'clamp(20px, 6vw, 30px)', 
            height: 'clamp(20px, 6vw, 30px)', 
            minWidth: '20px' 
          }} 
        />
        <h1 style={{ fontSize: 'clamp(20px, 6vw, 24px)', margin: 0 }}>SUN CO.</h1>
      </div>

      {/* Bouton View Chart aligné à droite avec espacement dynamique */}
      <button 
        onClick={() => navigate('/carte')} 
        style={{ 
          padding: '5px 20px', 
          border: '1px solid black',
          borderRadius: '8px', 
          color: 'black', 
          fontSize: 'clamp(14px, 3vw, 18px)', 
          cursor: 'pointer',
          margin: '0 clamp(20px, 10vw, 165px) 0 0', 
          background: '#fff',
          display: 'flex', 
          alignItems: 'center', 
          justifyContent: 'center',
          position: 'relative', 
        }}
      >
        View Cart
        
        {totalItems > 0 && (
          <span
            style={{
              maxHeight: '20px',
              maxWidth: '30px',
              borderRadius: '50%',
              marginLeft: '4px',
              background: 'red',
              color: 'white', 
              fontSize: 'clamp(12px, 2vw, 14px)',
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              padding: '4px', 
              transition: 'background 0.3s', 
            }}
            onMouseEnter={(e) => (e.target.style.background = 'darkred')} 
            onMouseLeave={(e) => (e.target.style.background = 'red')} 
          >
            {totalItems}
          </span>
        )}
      </button>
    </div>
  );
};

export default Header;