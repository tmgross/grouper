import React from 'react';
import axios from 'axios';
import { useState } from 'react';
import { Link } from 'react-router-dom';
import { IconButton } from '@mui/material';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import './center.css';

function LogInPage() {

  const [email, setEmail] = useState('');

  const handleLogin = async () => {
    axios.get(`http://localhost:8000/api/user/${email}`)
      .then(res => console.log(res.data))
      .catch(e => console.log(e))
  };


  return (
    <div className="centered">
      <Link to="/" className="go-back-button">
        <IconButton type="button"><ArrowBackIcon /></IconButton>
      </Link>
      <h1 className="location">Log In</h1>
      <div className="textbox-container">
        <input
          className="form-control nameIn"
          type="text"
          placeholder="Enter Email"
          onChange={(e) => setEmail(e.target.value)}
        />
        <button type="button" onClick={handleLogin}>
          Log In
        </button>
      </div>
    </div>
  );
}

export default LogInPage;
