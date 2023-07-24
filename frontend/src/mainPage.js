import './center.css';
import Button from '@mui/material/Button';
import React from 'react';
import { Link } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';

function Location() {

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
                    <button>Button 1</button>
                    <button>Button 2</button>
                    <button>Button 3</button>
                    <button>Button 4</button>
                </div>
            </div>
        </div>

        <div>
          <Link to="/group">
            <Button variant="contained" type="button" style={{width: '150px'}} >Create Group</Button>
          </Link>
        </div>

    </div>
  );
}

export default Location;
