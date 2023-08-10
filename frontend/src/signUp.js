import React from 'react';
import axios from 'axios';
import { useState } from 'react';
import { Link } from 'react-router-dom';
import { IconButton } from '@mui/material';
import Button from '@mui/material/Button';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import './center.css';

// Component for user sign-up
function SignUpPage() {
    const backendUrl = process.env.REACT_APP_BACKEND_URL;

    const [email, setEmail] = useState('');
    const [name, setName] = useState('');

    // Function to handle user sign-up
    const handleSignup = () => {
        axios.post(`${backendUrl}/api/user/`, { email, name })
            .then(res => {
                console.log(res.data);
                // navigate('/main'); UNCOMMENT THIS ONCE THERE ARE NO VALIDATION ERRORS
            })
            .catch(e => console.log(e))
    };

    return (
        <div className="centered fade-in">
            {/* Link to navigate back */}
            <Link to="/" className="go-back-button">
                <IconButton type="button"><ArrowBackIcon /></IconButton>
            </Link>
            {/* Page header */}
            <h1 className="location">Sign Up</h1>
            <div className="textbox-container">
                {/* Input field for entering email */}
                <input
                    className="form-control emailIn"
                    type="text"
                    placeholder="Enter Email"
                    onChange={(e) => setEmail(e.target.value)}
                />
                {/* Input field for entering name */}
                <input
                    className="form-control nameIn"
                    type="text"
                    placeholder="Enter Name"
                    onChange={(n) => setName(n.target.value)}
                />
                <Link to="/main"> {/* REMOVE THIS ONCE THERE ARE NO ERRORS */}
                    {/* Button to initiate sign-up */}
                    <Button variant="contained" type="button" style={{ width: '100px' }}
                        onClick={handleSignup}>
                        Sign Up
                    </Button>
                </Link>
            </div>
        </div>
    );
}

export default SignUpPage;
