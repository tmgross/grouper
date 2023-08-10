import './center.css';
import { Link } from 'react-router-dom';
import { IconButton } from '@mui/material';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import Button from '@mui/material/Button';
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';

function Location() {
  const backendUrl = process.env.REACT_APP_BACKEND_URL;

  const [name, setName] = useState('');
  const [locationName, setLocationName] = useState('');

  const joinLocation = () => {
    axios
      .put('${backendUrl}/api/user/adduser')
      .then(res => {
        console.log(res);
        // Do something on successful join
      })
      .catch(error => console.log(error));
  };

  const removeUserHandler = () => {
    axios
      .delete('${backendUrl}/api/user/remove')
      .then(res => console.log(res))
      .catch(error => console.log(error));
  };

  const getLocoName = async (locationid) => {
    axios.get(`${backendUrl}/api/user/location/loconame`)
      .then(res => {
        setLocationName(res.data); // Set the locationName state with the response data
      })
      .catch(e => console.log(e))
  };


  const getLocoUsers = async () => {
    try {
      const res = await axios.get('${backendUrl}/api/location/users');
      const users = res.data.join('\n'); // Join the array elements with newlines
      document.getElementById('whosHereTextBox').value = users;
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    getLocoName();
    getLocoUsers();
  }, []);

  const handleRefresh = () => {
    getLocoUsers();
  };


  return (
    <div className="centered">
      <Link to="/main" className="go-back-button">
        <IconButton type="button"><ArrowBackIcon /></IconButton>
      </Link>
      <h1 className="location">{locationName}</h1>

      <div style={{ display: 'flex', flexDirection: 'column' }}>
        <h2 style={{ alignSelf: 'flex-start', marginBottom: '5px' }}>Who's Here?</h2>
        <textarea
          id="whosHereTextBox"
          rows="10"
          cols="50"
          readOnly
          disabled
          style={{resize: 'none'}}
        >
          {getLocoUsers()}

        </textarea>
      </div>
      <div className="textbox-container">
        <input
          className="form-control nameIn"
          type="text"
          placeholder="Enter Name"
          onChange={event => setName(event.target.value)}
        />
        <Button variant="contained" type="button"  style={{width: '140px'}} onClick={joinLocation}>
          Join Group
        </Button>
        <Button variant="contained" type="button" style={{width: '140px'}} onClick={removeUserHandler}>
          Leave Group
        </Button>
        <Button variant="contained" type="button" style={{width: '140px'}} onClick={handleRefresh}>
          Refresh
        </Button>
      </div>
    </div>
  );
}

export default Location;
