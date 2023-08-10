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

    const handleInvite = async () => {
        //Replace this with proper function for inviting to group

        //   axios.get(`http://localhost:8000/api/user/${friend}`)
        //     .then(res => {
        //       console.log(res.data);
        //     })
        //     .catch(e => console.log(e))
    };

    return (
        <div className="centered">
            <Link to="/location" className="go-back-button">
                <IconButton type="button"><ArrowBackIcon /></IconButton>
            </Link>
            <h1 className="location">Invite to Group</h1>
            <h4>Select a friend or enter a friend code</h4>

            <div style={{ display: 'flex' }}>
                <div className="textbox-container">
                    <h2>Friends</h2>
                    <textarea
                        id="friendsTextBox"
                        rows="11"
                        cols="30"
                        readonly
                        disabled
                        className='friends-list'
                        style={{ resize: 'none' }}
                    >
                        This is a large text box that users can't edit.
                    </textarea>
                </div>
                <div className="textbox-container" style={{ marginTop: '130px' }}>
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
                            style={{ resize: 'none' }}
                        >
                            Friend Name
                        </textarea>
                    </div>
                    <Button variant="contained" type="button" style={{ width: '200px' }}
                        onClick={handleInvite}>
                        Send Invite
                    </Button>
                </div>
            </div>
        </div>
    );
}

export default GroupInvitePage;