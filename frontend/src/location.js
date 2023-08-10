import './center.css';
import { Link } from 'react-router-dom';
import { IconButton } from '@mui/material';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import Button from '@mui/material/Button';
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import { wait } from '@testing-library/user-event/dist/utils';

// Component for managing the current location
function Location() {
    const [locationName, setLocationName] = useState('');
    const [loading, setLoading] = useState(true); // Add a loading state


    // Function to join the current location
    const joinLocation = () => {
        axios
            .put('http://localhost:8000/api/user/adduser')
            .then(res => {
                console.log(res);
                // Do something on successful join
            })
            .catch(error => console.log(error));
    };

    // Function to remove the current user from the location
    const removeUserHandler = () => {
        axios
            .delete('http://localhost:8000/api/user/remove')
            .then(res => console.log(res))
            .catch(error => console.log(error));
    };

    // Function to get the location's name
    const getLocoName = async (locationid) => {
        axios.get(`http://localhost:8000/api/user/location/loconame`)
            .then(res => {
                setLocationName(res.data); // Set the locationName state with the response data
                setLoading(false);
            })
            .catch(e => {
                console.log(e)
                setLoading(false);
            })
    };

    // Function to get the users in the current location
    const getLocoUsers = async () => {
        try {
            const res = await axios.get('http://localhost:8000/api/location/users');
            const users = res.data.join('\n'); // Join the array elements with newlines
            document.getElementById('whosHereTextBox').value = users;
        } catch (error) {
            console.log(error);
        }
    };

    // Initial data retrieval
    useEffect(() => {
        getLocoName();
        getLocoUsers();
    }, []);

    // Function to handle refreshing the user list
    const handleRefresh = () => {
        getLocoUsers();
    };

    return (
        <div className="centered">
            {/* Links to navigate */}
            <Link to="/main" className="go-back-button">
                <IconButton type="button"><ArrowBackIcon /></IconButton>
            </Link>
            <Link to="/invitetogroup" className="log-out-button">
                <Button variant="contained" type="button">
                    Invite People
                </Button>
            </Link>
            {/* Display location name */}
            {!loading && (
                <div>
                    <h1 className="location">{locationName}</h1>
                </div>
            )}

            <div style={{ display: 'flex', flexDirection: 'column' }}>
                <h2 style={{ alignSelf: 'flex-start', marginBottom: '5px' }}>Who's Here?</h2>
                {/* Textarea to show users in the location */}
                <textarea
                    id="whosHereTextBox"
                    rows="10"
                    cols="50"
                    readOnly
                    disabled
                    style={{ resize: 'none' }}
                >
                    {getLocoUsers()}
                </textarea>
            </div>
            {/* Buttons for joining, leaving, and refreshing the group */}
            <Button variant="contained" type="button" style={{ width: '140px', marginTop: '10px' }}
                onClick={joinLocation}>
                Join Group
            </Button>
            <Button variant="contained" type="button" style={{ width: '140px', marginTop: '10px' }}
                onClick={removeUserHandler}>
                Leave Group
            </Button>
            <Button variant="contained" type="button" style={{ width: '140px', marginTop: '10px' }}
                onClick={handleRefresh}>
                Refresh
            </Button>
        </div>
    );
}

export default Location;
