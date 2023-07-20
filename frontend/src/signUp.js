import React from 'react';
import axios from 'axios';
import { useState } from 'react';
import { Link } from 'react-router-dom';
import { IconButton } from '@mui/material';
import Button from '@mui/material/Button';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import './center.css';

function SignUpPage() {

  const [email, setEmail] = useState('');
  const [name, setName] = useState('');


  const handleSignup = () => {
    axios.post(`http://localhost:8000/api/user/`, {email, name})
      .then(res => console.log(res.data))
      .catch(e => console.log(e))
  };


  return (
    <div className="centered">
      <Link to="/" className="go-back-button">
        <IconButton type="button"><ArrowBackIcon /></IconButton>
      </Link>
      <h1 className="location">Sign Up</h1>
      <div className="textbox-container">
        <input
          className="form-control emailIn"
          type="text"
          placeholder="Enter Email"
          onChange={(e) => setEmail(e.target.value)}
        />
        <input
          className="form-control nameIn"
          type="text"
          placeholder="Enter Name"
          onChange={(n) => setName(n.target.value)}
        />
        <Button variant="contained" type="button" onClick={handleSignup}>Log In</Button>
      </div>
    </div>
  );
}

export default SignUpPage;
