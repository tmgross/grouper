import './center.css';
import Button from '@mui/material/Button';
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Link } from 'react-router-dom';

function Location() {

  const [locations, setLocations] = useState({});

  useEffect(() => {
    // Fetch data from the API when the component mounts
    axios.get('http://localhost:8000/api/location/')
      .then(res => setLocations(res.data))
      .catch(e => console.log(e));
  }, []);

  const handleLocation = async (locationId) => {
    axios.get(`http://localhost:8000/api/user/${locationId}`)
      .then(res => {
        console.log(res.data);
        // navigate('/main') UNCOMMENT ONCE NO VALIDATION ERRORS
      })
      .catch(e => console.log(e))
  };


  return (
    <div className="centered">
      <h1 className="location company-name">grouper</h1>
        <div style={{ display: 'flex' }}>
            <div className="textbox-container">
                <h2>Your Friends</h2>
                <textarea
                    id="friendsTextBox"
                    rows="11"
                    cols="30"
                    readonly
                    disabled
                    className='friends-list'
                    style={{  resize: 'none' }}
                >
                This is a large text box that users can't edit.
                </textarea>
            </div>
         
            <div className="textbox-container">
                <h2>Your Groups</h2>
                <div class="button-container">
                  {Object.keys(locations).map(locationKey => (
                    <Link to="/location">
                      <button key={locationKey} onClick={() => handleLocation('64b6bfbb54263d417e25e9d1')}>
                        {/*locations[locationKey]*/locationKey} {locations[locationKey]}
                      </button>
                    </Link>
                  ))}
                </div>
            </div>
        </div>
    </div>
  );
}

export default Location;
