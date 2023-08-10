import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LandingPage from './landingPage';
import Location from './location';
import SignUp from './signUp';
import LogIn from './logIn';
import MainPage from './mainPage';
import GroupPage from './createGroup';
import FriendPage from './addFriend';
import InvitePage from './invites';
import GroupInvite from './groupInvite';


function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<LandingPage />} />
                <Route exact path="/location" element={<Location />} />
                <Route exact path="/signup" element={<SignUp />} />
                <Route exact path="/login" element={<LogIn />} />
                <Route exact path="/main" element={<MainPage />} />
                <Route exact path="/group" element={<GroupPage />} />
                <Route exact path="/friends" element={<FriendPage />} />
                <Route exact path="/invites" element={<InvitePage />} />
                <Route exact path="/invitetogroup" element={<GroupInvite />} />
            </Routes>
        </Router>
    );
}

export default App;