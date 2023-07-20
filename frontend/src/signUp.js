import React from 'react';
import axios from 'axios';
import { useState } from 'react';
import { Link } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';
import { IconButton } from '@mui/material';
import Button from '@mui/material/Button';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import './center.css';

function SignUpPage() {
  const [email, setEmail] = useState('');
  const [name, setName] = useState('');
  const navigate = useNavigate();

  const handleSignup = () => {
    axios.post(`http://localhost:8000/api/user/`, {email, name})
      .then(res => {
        console.log(res.data);
        //navigate('/main'); UNCOMMENT THIS ONCE THERE ARE NO VALIDATION ERRORS
      })
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
        <Link to="/main"> {/* REMOVE THIS ONCE THERE ARE NO ERRORS */}
          <Button variant="contained" type="button" onClick={handleSignup}>Sign Up</Button>
        </Link>
      </div>
    </div>
  );
}

export default SignUpPage;
