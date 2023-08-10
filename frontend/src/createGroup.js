import React from 'react';
import axios from 'axios';
import { useState } from 'react';
import { Link } from 'react-router-dom';
// import { useNavigate } from 'react-router-dom';
import { IconButton } from '@mui/material';
import Button from '@mui/material/Button';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import './center.css';

function NewGroupPage() {
  const backendUrl = process.env.REACT_APP_BACKEND_URL;

  const [group, setGroup] = useState('');
  // const navigate = useNavigate();

  const handleNewGroup = async () => {
    axios.post(`${backendUrl}/api/group/`, {group})
      .then(res => console.log(res.data))
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
          className="form-control emailIn"
          type="text"
          placeholder="Enter Group Name"
          onChange={(e) => setGroup(e.target.value)}
        />
        <Link to="/main">
          <Button variant="contained" type="button" onClick={handleNewGroup}>Create Group</Button>
        </Link>
      </div>
    </div>
  );
}

export default NewGroupPage;
