import React from 'react';
import { Link } from 'react-router-dom';
import Button from '@mui/material/Button';

function LandingPage() {
  return (
    <div className="centered">
      <h1>Grouper</h1>
      <div className="textbox-container">
        <div>
          <Link to="/signup">
            <Button variant="contained" type="button" >Sign Up</Button>
          </Link>
        </div>
        
        <div>
          <Link to="/login">
            <Button variant="contained" type="button">Log In</Button>
          </Link>
        </div>
      </div>
    </div>
  );
}

export default LandingPage;
