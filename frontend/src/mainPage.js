import './center.css';
import Button from '@mui/material/Button';
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';

function location() {

  const [locations, setLocations] = useState({});

  useEffect(() => {
    axios.get('http://localhost:8000/api/location/')
    .then(res => setLocations(res.data))
    .catch(e => console.log(e))
  });

  return (
    <div className="centered">
      <h1 className="location company-name">grouper</h1>
      <div className="textbox-container">
        <h2>Your Groups</h2>
        <div className="button-container">
            {Object.keys(locations).map(locationKey => (
            <button key={locationKey} onClick={() => console.log(locations[locationKey])}>
              {locations[locationKey].name}
            </button>
          ))}
            
            {/* <button>Button 1</button>
            <button>Button 2</button>
            <button>Button 3</button>
            <button>Button 4</button> */}
        </div>
      </div>
    </div>
  );
}

export default location;
