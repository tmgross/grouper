import React from 'react';
import axios from 'axios';
import { useState } from 'react';
import { Link } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';
import { IconButton } from '@mui/material';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import Button from '@mui/material/Button';
import './center.css';

function LogInPage() {
  const [group, setGroup] = useState('');
  const navigate = useNavigate();

  const handleGroup = async () => {
    axios.get(`http://localhost:8000/api/user/${group}`)
      .then(res => {
        console.log(res.data);
      })
      .catch(e => console.log(e))
  };

  return (
    <div className="centered">
      <Link to="/main" className="go-back-button">
        <IconButton type="button"><ArrowBackIcon /></IconButton>
      </Link>
      <h1 className="location">New Group</h1>
      <div className="textbox-container">
        <input
          className="form-control nameIn"
          type="text"
          placeholder="Enter Group Name"
          onChange={(e) => setGroup(e.target.value)}
        />
          <Button variant="contained" type="button" style={{width: '100px'}} onClick={handleGroup}>Create</Button>
        </div>
    </div>
  );
}

export default LogInPage;
