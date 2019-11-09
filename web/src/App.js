import React, {useState} from 'react'
import Favicon from './componentes/Favicon'
import ListaDePlantas from './componentes/ListaDePlantas'
import ListaDeEspacios from './componentes/ListaDeEspacios'
import HeaderBar from './componentes/HeaderBar'
import {Container, Row, Col} from 'reactstrap'
import Footer from './componentes/FooterBar'
import Grafico from './componentes/Grafico'
import 'bootstrap/dist/css/bootstrap.css'
import './css/listaCartas.css'
import './css/margenChart.css'
import './App.css'

function App() {
  const [espacios, setEspacios] = useState([])
  const [plantas, setPlantas] = useState([])
  const [espacioSeleccionado, setEspacioSeleccionado] = useState(null)
  const [plantaSeleccionada, setPlantaSeleccionada] = useState(null)
  const [dataPlanta, setDataPlanta] = useState({})

  return (
    <div className="App">
      <head>
        <Favicon />
      </head>
      <body>
        <HeaderBar />
          <div>
            <Container fluid= {true}>
              <Col>
                  <Row className='listaCartas' md={3}>
                    <ListaDeEspacios 
                      espacios={espacios} 
                      setEspacios={setEspacios} 
                      espacioSeleccionado={espacioSeleccionado} 
                      setEspacioSeleccionado={setEspacioSeleccionado} 
                    />
                  </Row>
                <Row className='listaCartas' md={3}>
                  <ListaDePlantas 
                    plantas={plantas} 
                    setPlantas={setPlantas} 
                    espacioSeleccionado={espacioSeleccionado}
                    plantaSeleccionada={plantaSeleccionada}
                    setPlantaSeleccionada={setPlantaSeleccionada}
                    setDataPlanta={setDataPlanta}
                    dataPlanta={dataPlanta}
                  />
                </Row>
                <Row className='margenChart' md={6}>
                  <h1>{dataPlanta.data}</h1>
                  <Grafico 
                    plantaSeleccionada={plantaSeleccionada}
                    espacioSeleccionado={espacioSeleccionado}
                    setDataPlanta={setDataPlanta}
                    dataPlanta={dataPlanta} />
                </Row>
              </Col>
            </Container>
          </div>
          <Footer/>
      </body>  
    </div>
  )
}

export default App
