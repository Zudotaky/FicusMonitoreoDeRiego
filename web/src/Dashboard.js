import React, { useState } from 'react'
import ListaDePlantas from './componentes/ListaDePlantas'
import ListaDeEspacios from './componentes/ListaDeEspacios'
import ColapsableSection from './componentes/ColapsableSection'
import {
  Container,
  Row,
  Col
} from 'reactstrap'
import Grafico from './componentes/Grafico'

function Dashboard() {
  const [espacios, setEspacios] = useState([])
  const [plantas, setPlantas] = useState([])
  const [espacioSeleccionado, setEspacioSeleccionado] = useState(null)
  const [plantaSeleccionada, setPlantaSeleccionada] = useState(null)
  const [dataPlanta, setDataPlanta] = useState({})

  return (
      <Container fluid>
        <Col>
          <Row className="listaCartas">
            <ColapsableSection title="Espacios">
              <ListaDeEspacios
                handleClick
                espacios={espacios}
                setEspacios={setEspacios}
                espacioSeleccionado={espacioSeleccionado}
                setEspacioSeleccionado={setEspacioSeleccionado}
              />
            </ColapsableSection>
          </Row>
          <Row className="listaCartas">
            <ColapsableSection title="Plantas">
              <ListaDePlantas
                plantas={plantas}
                setPlantas={setPlantas}
                espacioSeleccionado={espacioSeleccionado}
                plantaSeleccionada={plantaSeleccionada}
                setPlantaSeleccionada={setPlantaSeleccionada}
                setDataPlanta={setDataPlanta}
                dataPlanta={dataPlanta}
              />
            </ColapsableSection>
          </Row>
          <Row className="margenChart" style={{ display: 'block'}}>
            <ColapsableSection title="Gráfico">
              <Grafico
                plantaSeleccionada={plantaSeleccionada}
                espacioSeleccionado={espacioSeleccionado}
                setDataPlanta={setDataPlanta}
                dataPlanta={dataPlanta}
              />
            </ColapsableSection>
          </Row>
        </Col>
      </Container>
  )
}

export default Dashboard