import logo from './logo.svg';
import './App.css';

function MyButton() {
  return (
    <button>Guess the Country</button>
  );
}

function App() {
  return (
    <div className="App">
      
      <h1>Nationality Guessr </h1>
      <h2>Last Names Edition</h2>
      <MyButton />
    </div> 
    
  );
}

/*<header className="App-header">
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
      </header>*/

export default App;