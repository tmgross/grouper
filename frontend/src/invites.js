import './center.css';
import Button from '@mui/material/Button';
import axios from 'axios';
import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { IconButton } from '@mui/material';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import 'bootstrap/dist/css/bootstrap.min.css';

// Component for handling invites and requests
function InvitePage() {
    const [groupInvites, setGroupInvites] = useState({});

    useEffect(() => {
        fetchGroupInvites();
    }, []);

    const fetchGroupInvites = async () => {
        try {
            const response = await axios.get('http://localhost:8000/api/invites/get/groups');
            setGroupInvites(response.data);
        } catch (error) {
            console.error(error);
        }
    };

    const handleInvitationClick = async (fromId, fromName) => {
        // Handle the invitation click, e.g., accept or decline
        const response = await axios.post(`http://localhost:8000/api/invite/group/set/${fromId}`);
        console.log(`Accepted invitation from ${fromName} (ID: ${fromId})`);
    };

    const handleAcceptClick = async () => {
        try {
            const response = await axios.put('http://localhost:8000/api/invite/group/accept');
            const newId = response.data;
            if (newId != "invalid object") {
                // Handle successful accept (e.g., show a message to the user)
                console.log(`Accepted group invitation. New group ID: ${newId}`);
            } else {
                // Handle invalid object (e.g., show an error message)
                console.log("Invalid group invitation object.");
            }
        } catch (error) {
            console.error('Error while accepting invitation:', error);
        }
    };

    const handleRejectClick = async () => {
        try {
            const response = await axios.put('http://localhost:8000/api/invite/group/reject');
            if (response.data == "rejected") {
                // Handle successful reject (e.g., show a message to the user)
                console.log("Rejected group invitation.");
            } else {
                // Handle invalid object (e.g., show an error message)
                console.log("Invalid group invitation object.");
            }
        } catch (error) {
            console.error('Error while rejecting invitation:', error);
        }
    };



    return (
        <div className="centered">
            {/* Link to navigate back */}
            <Link to="/main" className="go-back-button">
                <IconButton type="button"><ArrowBackIcon /></IconButton>
            </Link>
            {/* Application title */}
            <h1 className="location company-name">grouper</h1>
            <h1>Invites and Requests</h1>
            <div style={{ display: 'flex' }}>
                {/* Container for friend requests */}
                <div className="textbox-container" style={{ marginLeft: '10px' }}>
                    <h2>Friend Requests</h2>
                    {/* Container for request buttons */}
                    <div className="button-container">
                        <button className="highlight-on-hover">Button 1</button>
                        <button className="highlight-on-hover">Button 2</button>
                        <button className="highlight-on-hover">Button 3</button>
                        <button className="highlight-on-hover">Button 4</button>
                    </div>
                </div>

                {/* Container for group invites */}
                <div className="textbox-container" style={{ marginLeft: '10px' }}>
                    <h2>Group Invites</h2>
                    {/* Container for invite buttons */}
                    <div className="button-container">
                        {Object.entries(groupInvites).map(([fromId, fromName]) => (
                            <button
                                key={fromId}
                                onClick={() => handleInvitationClick(fromId, fromName)}
                            >
                                {fromName}
                            </button>
                        ))}
      
                    </div>
                </div>
            </div>
            <div style={{
                display: 'grid', gridTemplateColumns: 'repeat(2, 2fr)',
                gap: '10px', marginLeft: '10px', marginTop: '10px'
            }} >
                {/* Buttons for handling requests and invites */}
                <Button variant="contained" type="button" style={{ width: '200px' }}>
                    Accept Request
                </Button>
                <Button variant="contained" type="button" style={{ width: '200px' }} onClick={handleAcceptClick} >
                    Accept Invite
                </Button>
                <Button variant="contained" type="button" style={{ width: '200px' }}>
                    Delete Request
                </Button>
                <Button variant="contained" type="button" style={{ width: '200px' }} onClick={handleRejectClick} >
                    Delete Invite
                </Button>
            </div>
        </div>
    );
}

export default InvitePage;
