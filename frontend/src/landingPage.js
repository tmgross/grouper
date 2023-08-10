import React from 'react';
import { Link } from 'react-router-dom';
import Button from '@mui/material/Button';
import './transitions.css'; // Import the animation styles

// Component for the landing page
function LandingPage() {
    return (
        <div className="centered fade-in">
            {/* Container for the application name and company */}
            <div className="name-container fade-in">
                <h1 className="name">grouper</h1>
                <h1 className="company-name">by GroupWare</h1>
            </div>
            {/* Slogan */}
            <h1 className="slogan">Bringing People Together</h1>
            <div className="textbox-container fade-in">
                <div>
                    {/* Link to the login page */}
                    <Link to="/login" className="fade-in">
                        <Button variant="contained" type="button" style={{ width: '100px' }}>
                            Log In
                        </Button>
                    </Link>
                </div>
                <div>
                    {/* Link to the signup page */}
                    <Link to="/signup" className="fade-in">
                        <Button variant="contained" type="button" style={{ width: '100px' }}>
                            Sign Up
                        </Button>
                    </Link>
                </div>
            </div>
        </div>
    );
}

export default LandingPage;
