import React from 'react';
import axios from 'axios';
import { useState } from 'react';
import { Link } from 'react-router-dom';
// import { useNavigate } from 'react-router-dom';
import { IconButton } from '@mui/material';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import Button from '@mui/material/Button';
import './center.css';
import './transitions.css';

// Component for user login
function LogInPage() {
    const backendUrl = process.env.REACT_APP_BACKEND_URL;
    const [email, setEmail] = useState('');
    // const navigate = useNavigate();

    // Function to handle user login
    const handleLogin = async () => {
        try {
            const response = await axios.get(`${backendUrl}/api/user/${email}`);
            console.log(response.data);
            // navigate('/main') UNCOMMENT ONCE NO VALIDATION ERRORS
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div className="centered fade-in">
            {/* Link to navigate back */}
            <Link to="/" className="go-back-button">
                <IconButton type="button"><ArrowBackIcon /></IconButton>
            </Link>
            {/* Page header */}
            <h1 className="location">Log In</h1>
            <div className="textbox-container">
                {/* Input field for entering email */}
                <input
                    className="form-control nameIn"
                    type="text"
                    placeholder="Enter Email"
                    onChange={(e) => setEmail(e.target.value)}
                />
                {/* Button to initiate login */}
                <Link to="/main"> {/* REMOVE THIS ONCE THERE ARE NO ERRORS */}
                    <Button variant="contained" type="button" style={{ width: '100px' }}
                        onClick={handleLogin}>
                        Log In
                    </Button>
                </Link>
            </div>
        </div>
    );
}

export default LogInPage;
