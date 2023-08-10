import React from 'react';
import axios from 'axios';
import { useState } from 'react';
import { Link } from 'react-router-dom';
import { IconButton } from '@mui/material';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import Button from '@mui/material/Button';
import './center.css';

// Component for adding friends
function AddFriendPage() {
    const backendUrl = process.env.REACT_APP_BACKEND_URL;
    // State to store friend's code
    const [friend, setFriend] = useState('');

    // Function to handle fetching friend information
    const handleFriend = async () => {
        try {
            const response = await axios.get(`${backendUrl}/api/user/${friend}`);
            console.log(response.data);
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div className="centered">
            {/* Link to navigate back */}
            <Link to="/main" className="go-back-button">
                <IconButton type="button"><ArrowBackIcon /></IconButton>
            </Link>
            {/* Page header */}
            <h1 className="location">Add Friends</h1>
            <div className="textbox-container">
                {/* Input field for entering friend code */}
                <input
                    className="form-control nameIn"
                    type="text"
                    placeholder="Enter Friend Code"
                    onChange={(e) => setFriend(e.target.value)}
                />
                <div className="textbox-container">
                    {/* Display friend's name */}
                    <text>
                        This code belongs to:
                    </text>
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
                {/* Button to send friend request */}
                <Button variant="contained" type="button" style={{ width: '200px' }}
                    onClick={handleFriend}>
                    Send Friend Request
                </Button>
            </div>
        </div>
    );
}

export default AddFriendPage;
