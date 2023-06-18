import logo from './logo.svg';
import './App.css';
import AddButton from './components/AddButton.tsx'
import RemoveButton from './components/RemoveButton.tsx'
import Header from './components/Header.tsx'
import InputBox from './components/InputBox.tsx'


function App(){
  return (<div><Header  />
  <InputBox/>
  <AddButton/>
  <RemoveButton/>
  </div>
  
  )
}

export default App;

/*
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
*/