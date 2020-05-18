import React from 'react';
import {BrowserRouter, Route} from 'react-router-dom';
import Main from './Pages/Main/Main';


function App() {
  return (
    <div className="App">
    <BrowserRouter>  
      <Route path='/' component={Main} exact={true}  />
    </BrowserRouter>
    </div>
  );
}

export default App;
