import React from 'react';
import axios from 'axios';
import { useState } from 'react';
import { Link } from 'react-router-dom';
import { IconButton } from '@mui/material';
import Button from '@mui/material/Button';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import './center.css';

// Component for creating a new group
function NewGroupPage() {
    // State to store the new group name
    const [group, setGroup] = useState('');

    // Function to handle creating a new group
    const handleNewGroup = async () => {
        try {
            const response = await axios.post(`http://localhost:8000/api/group/`, { group });
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
            <h1 className="location">New Group</h1>
            <div className="textbox-container">
                {/* Input field for entering new group name */}
                <input
                    className="form-control emailIn"
                    type="text"
                    placeholder="Enter Group Name"
                    onChange={(e) => setGroup(e.target.value)}
                />
                {/* Button to create the new group */}
                <Link to="/main">
                    <Button variant="contained" type="button" onClick={handleNewGroup}>
                        Create Group
                    </Button>
                </Link>
            </div>
        </div>
    );
}

export default NewGroupPage;
