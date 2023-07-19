import React from 'react';
import { Link } from 'react-router-dom';
import './center.css';


function SignUpPage() {
  return (
    <div className="centered">
      <h1 className="location">Sign Up</h1>
      <div className="textbox-container">
        <input
          className="form-control nameIn"
          type="text"
          placeholder="Enter Name"
        />
        <input
          className="form-control nameIn"
          type="text"
          placeholder="Enter Email"
        />
        <button type="button" >
          Sign Up
        </button>
        <Link to="/">
          <button type="button">Go Back</button>
        </Link>
      </div>
    </div>

  );
}

export default SignUpPage;
