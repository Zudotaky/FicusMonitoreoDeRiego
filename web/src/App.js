import React from 'react';
import './App.css';
import Favicon from './Favicon';
import Plant from './Plant';
import DataChart from './DataChart';
import HeaderBar from './HeaderBar';
function App() {
  return (

      <div className="App">
        <head>
          <Favicon />
        </head>
        <body>
        <HeaderBar />
         <div class="row">
         <div class="column">
              <Plant />
              <Plant />
              <Plant />
            </div>
            <div class="column">
              <DataChart />
            </div>
          </div>
        </body>  
    </div>
  );
}

export default App;
