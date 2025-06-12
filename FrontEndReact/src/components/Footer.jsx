import { Radius } from 'lucide-react';
import React from 'react';
import { FaTelegram, FaTwitter, FaYoutube } from 'react-icons/fa'; // Import des icônes

const Footer = () => {
  return (
    <footer style={{ 
      display: 'flex', 
      justifyContent: 'space-between', 
      alignItems: 'center', 
      padding: '20px', 
      backgroundColor: '#000', 
      color: '#fff', 
      fontSize: 'clamp(12px, 2vw, 16px)',
      marginTop: 'auto',
      flexWrap: 'wrap', 
      gap: '10px' 
    }}>
      {/* Section droite : SUN CO. */}
              <div style={{ 
          order: 1, 
          display: 'flex', 
          alignItems: 'center',
          paddingLeft:'clamp(100px, 2vw, 16px)',
          margin:0,
        }}>
          <img 
            src="image/Image8.png" 
            alt="Promo Image" 
            style={{ 
              width: 'clamp(20px, 6vw, 20px)', 
              height: 'clamp(20px, 6vw, 20px)', 
              marginRight: '8px'
            }} 
          />
          <p style={{ 
            margin: 0, 
           
            fontSize: 'clamp(10px, 3vw, 16px)' 
          }}>
            SUN CO.
          </p>
        </div>

      {/* Section centre : Texte */}
      <div style={{ order: 2,  textAlign: 'center', }}>
        <p style={{ margin: 0 }}>© 2023 dot.cards text task.</p>
      </div>
      {/* Section gauche : Icônes */}
      <div style={{ display: 'flex', gap: '20px', order: 3, paddingRight:'clamp(100px, 2vw, 16px)', }}>
  {/* Icône Telegram */}
        <a href="https://telegram.org" target="_blank" rel="noopener noreferrer" style={{ color: '#fff', background: 'gray', borderRadius: '50%', padding: '4px', display: 'flex', alignItems: 'center', justifyContent: 'center', transition: 'background 0.3s' }}>
          <FaTelegram size={15} />
        </a>

        {/* Icône Twitter */}
        <a href="https://twitter.com" target="_blank" rel="noopener noreferrer" style={{ color: '#fff', background: 'gray', borderRadius: '50%', padding: '4px', display: 'flex', alignItems: 'center', justifyContent: 'center', transition: 'background 0.3s' }}>
          <FaTwitter size={15} />
        </a>

        {/* Icône YouTube */}
        <a href="https://youtube.com" target="_blank" rel="noopener noreferrer" style={{ color: '#fff', background: 'gray', borderRadius: '50%', padding: '4px', display: 'flex', alignItems: 'center', justifyContent: 'center', transition: 'background 0.3s' }}>
          <FaYoutube size={15} />
        </a>
</div>
    </footer>
  );
};

export default Footer;