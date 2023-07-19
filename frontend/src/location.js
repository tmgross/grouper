import './center.css';
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

  return (
    <div className="centered">
      <h1 className="location">Union</h1>
      <div className="textbox-container">
        <input
          className="form-control nameIn"
          type="text"
          placeholder="Enter Name"
          onChange={event => setName(event.target.value)}
        />
        <button type="button" onClick={addUserHandler}>
          Join Group
        </button>
        <button type="button" onClick={removeUserHandler}>
          Leave Group
        </button>
      </div>
    </div>
  );
}

export default location;
