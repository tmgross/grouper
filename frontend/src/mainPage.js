import './center.css';
import React, { useState, useEffect } from 'react';
import Button from '@mui/material/Button';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Link } from 'react-router-dom';

function MainPage() {
  const backendUrl = process.env.REACT_APP_BACKEND_URL;

  const [locations, setLocations] = useState({});

  useEffect(() => {
    // Fetch data from the API when the component mounts
    axios.get(`${backendUrl}/api/location/`)
      .then(res => setLocations(res.data))
      .catch(e => console.log(e));
  }, []);

  const handleLocation = async (locationId) => {
    axios.get(`${backendUrl}/api/user/loco/${locationId}`)
      .then(res => {
        console.log(res.data);
        // navigate('/main') UNCOMMENT ONCE NO VALIDATION ERRORS
      })
      .catch(e => console.log(e))
  };

  // const getUserName = async () => {
  //   try {
  //     const res = await axios.get('${backendUrl}/api/username');
  //     setUserName(res.data);
  //   } catch (error) {
  //     console.log(error);
  //   }
  // };

  return (
    <div className="centered">
      <Link to="/" className="log-out-button">
        <Button variant="contained" type="button">Log Out</Button>
      </Link>
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
                      <button key={locationKey} onClick={() => handleLocation(locationKey)}>
                        {locations[locationKey]}
                      </button>
                    </Link>
                  ))}
                </div>
            </div>
        </div>
        <div>
          <div style={{marginTop:'10px'}}>
            <Link to="/friends">
              <Button variant="contained" type="button" style={{width: '150px', height: '60px', marginRight: '10px'}} >Add Friend</Button>
            </Link>
            <Link to="/invites">
              <Button variant="contained" type="button" style={{width: '175px', height: '60px', marginRight: '10px'}} >Invites and Friend Requests</Button>
            </Link>
            <Link to="/group">
              <Button variant="contained" type="button" style={{width: '150px', height: '60px'}} >Create Group</Button>
            </Link>
          </div>
        </div>
    </div>
  );
}

export default MainPage;
