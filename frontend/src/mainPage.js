import './center.css';
import React, { useState, useEffect } from 'react';
import Button from '@mui/material/Button';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Link } from 'react-router-dom';

// Component for the main page
function MainPage() {
    const [locations, setLocations] = useState({});
    const [friendCode, setFriendCode] = useState('');
    const [loading, setLoading] = useState(true); // Add a loading state

    useEffect(() => {
        // Fetch data from the API when the component mounts
        axios.get('http://localhost:8000/api/location/')
            .then(res => setLocations(res.data))
            .catch(e => console.log(e));

        // Fetch the current user's friend code from the server
        axios.get('http://localhost:8000/api/email')
            .then(res => {
                setFriendCode(res.data);
                setLoading(false); // Set loading to false when the data is retrieved
            })
            .catch(e => {
                console.log(e);
                setLoading(false); // Set loading to false in case of an error
            });
    }, []);

    const handleLocation = async (locationId) => {
        axios.get(`http://localhost:8000/api/user/loco/${locationId}`)
            .then(res => {
                console.log(res.data);
                // navigate('/main') UNCOMMENT ONCE NO VALIDATION ERRORS
            })
            .catch(e => console.log(e))
    };

    // Get the friends list
    const [friends, setFriends] = useState([]);

    useEffect(() => {
        // Fetch friends data from the API when the component mounts
        axios.get('http://localhost:8000/api/friends/')
            .then(res => setFriends(res.data))
            .catch(e => console.log(e));
    }, []);

    return (
        <div className="centered fade-in">
            {/* Link to log out */}
            <Link to="/" className="log-out-button">
                <Button variant="contained" type="button">
                    Log Out
                </Button>
            </Link>
            {/* Display friend code */}
            {!loading && (
                <div className="go-back-button" style={{
                    fontFamily: '"Trebuchet MS", Helvetica, sans-serif',
                    fontSize: '20px'
                }}>
                    Friend Code: {friendCode}
                </div>
            )}
            {/* Application title */}
            <h1 className="location company-name">grouper</h1>

            <div style={{ display: 'flex' }}>
                {/* Container for displaying friends */}
                <div className="textbox-container">
                    <h2>Your Friends</h2>
                    {/* Textarea to show friends */}
                    <textarea
                        id="friendsTextBox"
                        rows="11"
                        cols="30"
                        readOnly
                        disabled
                        className='friends-list'
                        style={{ resize: 'none' }}
                        value={friends.join('\n')}  /* Join the friends array with line breaks */
                    >
                        {/* Placeholder text */}
                        This is the friends text box.
                    </textarea>
                </div>

                {/* Container for displaying groups */}
                <div className="textbox-container">
                    <h2>Your Groups</h2>
                    <div className="button-container">
                        {/* Display the list of groups */}
                        {Object.keys(locations).map(locationKey => (
                            <Link to="/location">
                                <button key={locationKey} onClick={() => handleLocation(locationKey)}>
                                    {locations[locationKey]}
                                </button>
                            </Link>
                        ))}
                    </div>
                </div>
            </div>
            <div>
                <div style={{ marginTop: '10px' }}>
                    {/* Buttons for navigating to different pages */}
                    <Link to="/friends">
                        <Button variant="contained" type="button"
                            style={{ width: '150px', height: '60px', marginRight: '10px' }}>
                            Add Friend
                        </Button>
                    </Link>
                    <Link to="/invites">
                        <Button variant="contained" type="button"
                            style={{ width: '175px', height: '60px', marginRight: '10px' }}>
                            Invites and Friend Requests
                        </Button>
                    </Link>
                    <Link to="/group">
                        <Button variant="contained" type="button"
                            style={{ width: '150px', height: '60px' }}>
                            Create Group
                        </Button>
                    </Link>
                </div>
            </div>
        </div>
    );
}

export default MainPage;
