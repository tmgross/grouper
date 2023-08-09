import './center.css';
import Button from '@mui/material/Button';
import React from 'react';
import { Link } from 'react-router-dom';
import { IconButton } from '@mui/material';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import 'bootstrap/dist/css/bootstrap.min.css';

function InvitePage() {
  return (
    <div className="centered">
      <Link to="/main" className="go-back-button">
        <IconButton type="button"><ArrowBackIcon /></IconButton>
      </Link>
      <h1 className="location company-name">grouper</h1>
      <h1>Invites and Requests</h1>
        <div style={{ display: 'flex' }}>
        <div className="textbox-container" style={{marginLeft:'10px'}}>
                <h2>Friend Requests</h2>
                <div class="button-container">
                    <button className="highlight-on-hover">Button 1</button>
                    <button className="highlight-on-hover">Button 2</button>
                    <button className="highlight-on-hover">Button 3</button>
                    <button className="highlight-on-hover">Button 4</button>
                </div>
            </div>

            <div className="textbox-container" style={{marginLeft:'10px'}}>
                <h2>Group Invites</h2>
                <div class="button-container">
                    <button className="highlight-on-hover">Button 1</button>
                    <button className="highlight-on-hover">Button 2</button>
                    <button className="highlight-on-hover">Button 3</button>
                    <button className="highlight-on-hover">Button 4</button>
                </div>
            </div>
        </div>
        <div style={{display: 'grid', gridTemplateColumns: 'repeat(2, 2fr)', 
                     gap: '10px', marginLeft: '10px', marginTop: '10px'}} >
          <Button variant="contained" type="button" style={{ width: '200px' }}>
            Accept Request
          </Button>
          <Button variant="contained" type="button" style={{ width: '200px' }}>
            Accept Invite
          </Button>
          <Button variant="contained" type="button" style={{ width: '200px' }}>
            Delete Request
          </Button>
          <Button variant="contained" type="button" style={{ width: '200px' }}>
            Delete Invite
          </Button>
        </div>
    </div>
  );
}

export default InvitePage;