import React from 'react';
import './App.css';
import Favicon from './componentes/Favicon';
import Plant from './componentes/Plant';
import DataChart from './componentes/DataChart';
import HeaderBar from './componentes/HeaderBar';
function App() {
  return (

    <div className="App">
        <head>
          <Favicon />
        </head>
        <body>
          <HeaderBar />
          <div className="row">
            <div className="column">
              <Plant />
              <Plant />
              <Plant />
            </div>
            <div className="column">
              <DataChart />
            </div>
          </div>
        </body>  
    </div>
  );
}

export default App;
