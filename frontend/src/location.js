import './center.css';
import { Link } from 'react-router-dom';
import { IconButton } from '@mui/material';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import Button from '@mui/material/Button';
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';

function location() {
  const [name, setName] = useState('');

  const addUserHandler = () => {
    axios
      .post('http://localhost:8000/api/user/', { name: name })
      .then(res => console.log(res))
      .catch(error => console.log(error));
  };

  const removeUserHandler = () => {
    axios
      .post('http://localhost:8000/api/user/rm', { name: name })
      .then(res => console.log(res))
      .catch(error => console.log(error));
  };

  const getLocoName = async (locationid) => {
    axios.get(`/api/user/loconame`)
      .then(res => {
        console.log(res.data);
        // navigate('/main') UNCOMMENT ONCE NO VALIDATION ERRORS
      })
      .catch(e => console.log(e))
  };


  return (
    <div className="centered">
      <Link to="/main" className="go-back-button">
        <IconButton type="button"><ArrowBackIcon /></IconButton>
      </Link>
      <h1 className="location">Location</h1>
      <div style={{ display: 'flex', flexDirection: 'column' }}>
        <h2 style={{ alignSelf: 'flex-start', marginBottom: '5px' }}>Who's Here?</h2>
        <textarea
          id="whosHereTextBox"
          rows="10"
          cols="50"
          readonly
          disabled
          style={{resize: 'none'}}
        >
          This is a large text box that users can't edit.
        </textarea>
      </div>
      <div className="textbox-container">
        <input
          className="form-control nameIn"
          type="text"
          placeholder="Enter Name"
          onChange={event => setName(event.target.value)}
        />
        <Button variant="contained" type="button"  style={{width: '140px'}} onClick={addUserHandler}>
          Join Group
        </Button>
        <Button variant="contained" type="button" style={{width: '140px'}} onClick={removeUserHandler}>
          Leave Group
        </Button>
      </div>
    </div>
  );
}

export default location;
