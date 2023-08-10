import React from 'react';
import axios from 'axios';
import { useState } from 'react';
import { Link } from 'react-router-dom';
import { IconButton } from '@mui/material';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import Button from '@mui/material/Button';
import './center.css';

// Component for inviting friends to a group
function GroupInvitePage() {
    const [friend, setFriend] = useState('');

    // Function to handle sending group invite
    const handleInvite = async () => {
        try {
            // Replace this with proper function for inviting to group
            // Example:
            // const response = await axios.post(`http://localhost:8000/api/group/invite`, { friend });
            // console.log(response.data);
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div className="centered">
            {/* Link to navigate back */}
            <Link to="/location" className="go-back-button">
                <IconButton type="button"><ArrowBackIcon /></IconButton>
            </Link>
            {/* Page header */}
            <h1 className="location">Invite to Group</h1>
            <h4>Select a friend or enter a friend code</h4>

            <div style={{ display: 'flex' }}>
                {/* Container for displaying friends */}
                <div className="textbox-container">
                    <h2>Friends</h2>
                    <textarea
                        id="friendsTextBox"
                        rows="11"
                        cols="30"
                        readOnly
                        disabled
                        className='friends-list'
                        style={{ resize: 'none' }}
                    >
                        {/* Placeholder text */}
                        This is a large text box that users can't edit.
                    </textarea>
                </div>
                {/* Container for sending invites */}
                <div className="textbox-container" style={{ marginTop: '130px' }}>
                    {/* Input field for entering friend code */}
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
                        {/* Display friend's name */}
                        <textarea
                            id="friendsNameTextBox"
                            readOnly
                            disabled
                            className='friends-name'
                            style={{ resize: 'none' }}
                        >
                            Friend Name
                        </textarea>
                    </div>
                    {/* Button to send the group invite */}
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
