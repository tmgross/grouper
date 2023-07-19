import React from 'react';
import { Link } from 'react-router-dom';
import './center.css';


function LogUpPage() {
  return (
    <div className="centered">
      <h1 className="location">Log In</h1>
      <div className="textbox-container">
        <input
          className="form-control nameIn"
          type="text"
          placeholder="Enter Email"
        />
        <button type="button" >
          Log In
        </button>
        <Link to="/">
          <button type="button">Go Back</button>
        </Link>
      </div>
    </div>

  );
}

export default LogUpPage;
