import React from 'react';
import { Link } from 'react-router-dom';

function LandingPage() {
  return (
    <div className="centered">
      <h1>Grouper</h1>
      <div className="button-container">
        <div>
          <Link to="/signup">
            <button type="button">Sign Up</button>
          </Link>
        </div>
        
        <div>
          <Link to="/login">
            <button type="button">Log In</button>
          </Link>
        </div>
      </div>
    </div>
  );
}

export default LandingPage;
