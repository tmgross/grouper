import React from 'react';
import axios from 'axios';
import { useState } from 'react';
import { Link } from 'react-router-dom';
import { IconButton } from '@mui/material';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import Button from '@mui/material/Button';
import './center.css';

function GroupInvitePage() {
    const [friend, setFriend] = useState('');

    const handleFriend = async () => {
      axios.get(`http://localhost:8000/api/user/${friend}`)
        .then(res => {
          console.log(res.data);
        })
        .catch(e => console.log(e))
    };

  return (
    <div className="centered">
      <Link to="/location" className="go-back-button">
        <IconButton type="button"><ArrowBackIcon /></IconButton>
      </Link>
      <h1 className="location">Invite to Group</h1>
      <h4>Select a friend or enter a friend code</h4>

      <div className="textbox-container">
        <input
          className="form-control nameIn"
          type="text"
          placeholder="Enter Friend Code"
          onChange={(e) => setFriend(e.target.value)}
        />

        <div className="textbox-container">
                <text>
                    This code belongs to:
                </text>
                <textarea
                  id="friendsNameTextBox"
                  readonly
                  disabled
                  className='friends-name'
                  style={{  resize: 'none' }}
                >
                  Friend Name
                </textarea>
            </div>
          <Button variant="contained" type="button" style={{width: '200px'}} 
          onClick={handleFriend}>
            Send Invite
          </Button>
        </div>


    </div>
  );
}

export default GroupInvitePage;