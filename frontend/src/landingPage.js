import React from 'react';
import { Link } from 'react-router-dom';
import Button from '@mui/material/Button';

function LandingPage() {
  return (
    <div className="centered">
      <div className="name-container">
        <h1 className="name">grouper</h1>
        <h1 className="company-name">by GroupWare</h1>
      </div>
        <h1 className="slogan">Bringing People Together</h1>
      <div className="textbox-container">
        <div>
          <Link to="/login">
            <Button variant="contained" type="button" style={{width: '100px'}}>Log In</Button>
          </Link>
        </div>

        <div>
          <Link to="/signup">
            <Button variant="contained" type="button" style={{width: '100px'}}>Sign Up</Button>
          </Link>
        </div>
      </div>
    </div>
  );
}

export default LandingPage;
