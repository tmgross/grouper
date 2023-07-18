import logo from './logo.svg';
import './App.css';

import React, {useState, useEffect} from 'react';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css'

import AddButton from './components/AddButton.tsx'
import RemoveButton from './components/RemoveButton.tsx'
import Header from './components/Header.tsx'
import InputBox from './components/InputBox.tsx'



function App(){

  // const [userList, setUserList] = useState([{}]);
  const [name, setName] = useState('');

/*
  // get all users
  useEffect( () => {
    axios.get('https://localhost:8000/api/user')
    .then(res => {
      setUserList(res.data)
    })
  });*/

  // add a user
  const addUserHandler = () => {
    axios.post('http://localhost:8000/api/user/', {'name': name})
    .then(res => console.log(res))
    .catch(error => console.log(error))
  };



return (
  <div>
    <Header/>
    <input 
      className="form-control nameIn" type="text" placeholder="Enter Name" onChange={event => setName(event.target.value)}/> 
    <button 
      type="button" 
      onClick={addUserHandler}
    >
      Join Group
    </button>
    <RemoveButton/>
  </div>
  )
}

export default App;
