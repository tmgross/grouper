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
  const [friend, setFriend] = useState('');
  const navigate = useNavigate();

  const handleFriend = async () => {
    axios.get(`http://localhost:8000/api/user/${friend}`)
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
      <h1 className="location">Add Friends</h1>
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


          <Button variant="contained" type="button" style={{width: '200px'}} onClick={handleFriend}>Send Friend Request</Button>
        </div>
    </div>
  );
}

export default LogInPage;
