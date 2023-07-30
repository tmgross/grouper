import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LandingPage from './landingPage';
import Location from './location';
import SignUp from './signUp';
import LogIn from './logIn';
import MainPage from './mainPage';




function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LandingPage />}/>
        <Route exact path="/location" element={<Location />} />
        <Route exact path="/signup" element={<SignUp />} />
        <Route exact path="/login" element={<LogIn />} />
        <Route exact path="/main" element={<MainPage />} />
      </Routes>
    </Router>
  );
}

export default App;