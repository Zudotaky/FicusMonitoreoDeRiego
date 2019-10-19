import React from 'react';
import './App.css';
import Favicon from './componentes/Favicon';
import ListaDePlantas from './componentes/ListaDePlantas'
import ListaDeEspacios from './componentes/ListaDeEspacios'
import DataChart from './componentes/DataChart';
import HeaderBar from './componentes/HeaderBar';
import {Container, Row, Col} from 'reactstrap'
import 'bootstrap/dist/css/bootstrap.css';

function App() {
  return (

    <div className="App">
      <head>
        <Favicon />
      </head>
      <body>
        <HeaderBar />
          <div>
            <Container fluid= {true}>
              <Row>
                <Col md={2.5}>
                  <ListaDeEspacios />
                </Col>
                <Col md={2.5}>
                  <ListaDePlantas />
                </Col>
                <Col md={6}>
                  <DataChart />
                </Col>
              </Row>
            </Container>
          </div>
      </body>  
    </div>
  );
}

export default App;
