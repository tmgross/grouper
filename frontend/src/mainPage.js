import './center.css';
import Button from '@mui/material/Button';
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';

function location() {

  return (
    <div className="centered">
      <h1 className="location company-name">grouper</h1>
      <div className="textbox-container">
        <h2>Your Groups</h2>
        <div class="button-container">
            <button>Button 1</button>
            <button>Button 2</button>
            <button>Button 3</button>
            <button>Button 4</button>
        </div>
      </div>
    </div>
  );
}

export default location;
