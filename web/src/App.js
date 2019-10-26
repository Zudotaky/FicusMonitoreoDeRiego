import React, {useState} from 'react';
import './App.css';
import Favicon from './componentes/Favicon';
import ListaDePlantas from './componentes/ListaDePlantas'
import ListaDeEspacios from './componentes/ListaDeEspacios'
import DataChart from './componentes/DataChart';
import HeaderBar from './componentes/HeaderBar';
import {Container, Row, Col} from 'reactstrap'
import 'bootstrap/dist/css/bootstrap.css';
import Grafico from './componentes/Grafico';

function App() {
  const [espacios, setEspacios] = useState([]);
  const [plantas, setPlantas] = useState([]);
  const [espacioSeleccionado, setEspacioSeleccionado] = useState(null)
  const [plantaSeleccionada, setPlantaSeleccionada] = useState(null)
  const [dataPlanta, setDataPlanta] = useState(null)

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
                <Col md={3}>
                  <ListaDeEspacios 
                    espacios={espacios} 
                    setEspacios={setEspacios} 
                    espacioSeleccionado={espacioSeleccionado} 
                    setEspacioSeleccionado={setEspacioSeleccionado} 
                  />
                </Col>
                <Col md={3}>
                  <ListaDePlantas 
                    plantas={plantas} 
                    setPlantas={setPlantas} 
                    espacioSeleccionado={espacioSeleccionado}
                    plantaSeleccionada={plantaSeleccionada}
                    setPlantaSeleccionada={setPlantaSeleccionada}
                    setDataPlanta={setDataPlanta}
                  />
                </Col>
                <Col md={6}>
                <Grafico plantaSeleccionada={plantaSeleccionada} setDataPlanta={setDataPlanta} dataPlanta={dataPlanta} />
                </Col>
              </Row>
            </Container>
          </div>
      </body>  
    </div>
  );
}

export default App;
