import React from 'react';
import { Link } from 'react-router-dom';
import { IconButton } from '@mui/material';
import Button from '@mui/material/Button';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import './center.css';

function SignUpPage() {
  return (
    <div className="centered">
      <Link to="/" className="go-back-button">
        <IconButton type="button"><ArrowBackIcon /></IconButton>
      </Link>
      <h1 className="location">Sign Up</h1>
      <div className="textbox-container">
        <input
          className="form-control nameIn"
          type="text"
          placeholder="Enter Email"
        />
        <Button variant="contained" type="button">Log In</Button>
      </div>
    </div>
  );
}

export default SignUpPage;
