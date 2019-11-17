import React, { useState } from 'react';
import ListaDePlantas from './componentes/ListaDePlantas';
import ListaDeEspacios from './componentes/ListaDeEspacios';
import {
  Container,
  Row,
  Col,
  Collapse,
  CardBody,
  Card,
  CardText,
  CardTitle
} from 'reactstrap';
import Grafico from './componentes/Grafico';

function Dashboard() {
  const [espacios, setEspacios] = useState([])
  const [plantas, setPlantas] = useState([])
  const [espacioSeleccionado, setEspacioSeleccionado] = useState(null)
  const [plantaSeleccionada, setPlantaSeleccionada] = useState(null)
  const [dataPlanta, setDataPlanta] = useState({})

  const [isOpenEspacios, setIsOpenEspacios] = useState(false)
  const [isOpenPlantas, setIsOpenPlantas] = useState(false)
  const [isOpenGrafico, setIsOpenGrafico] = useState(false)
  const toggleEspacios = () => setIsOpenEspacios(!isOpenEspacios)
  const togglePlantas = () => setIsOpenPlantas(!isOpenPlantas)
  const toggleGrafico = () => setIsOpenGrafico(!isOpenGrafico)

  return (
        <div>
          <Container fluid={true}>
            <Col>
              <Row className="listaCartas" md={3}>
                <Card style={{ backgroundColor: 'lightgreen'}}>
                  <CardBody>
                    <CardTitle style={{ backgroundColor: 'lightgray' }}>
                      <div
                        onClick={toggleEspacios}
                        style={{ backgroundColor: 'blue' }}
                      >
                        Espacios
                      </div>
                    </CardTitle>
                    <CardText>
                      <Collapse isOpen={isOpenEspacios}>
                        <ListaDeEspacios
                          handleClick
                          espacios={espacios}
                          setEspacios={setEspacios}
                          espacioSeleccionado={espacioSeleccionado}
                          setEspacioSeleccionado={setEspacioSeleccionado}
                        />
                      </Collapse>
                    </CardText>
                  </CardBody>
                </Card>
              </Row>
              <Row className="listaCartas">
                <Card style={{ backgroundColor: 'lightgreen' }}>
                  <CardBody>
                    <CardTitle style={{ backgroundColor: 'lightgray' }}>
                      <div
                        onClick={togglePlantas}
                        style={{ backgroundColor: 'blue' }}
                      >
                        Plantas
                      </div>
                    </CardTitle>
                    <CardText>
                      <Collapse isOpen={isOpenPlantas}>
                        <ListaDePlantas
                          plantas={plantas}
                          setPlantas={setPlantas}
                          espacioSeleccionado={espacioSeleccionado}
                          plantaSeleccionada={plantaSeleccionada}
                          setPlantaSeleccionada={setPlantaSeleccionada}
                          setDataPlanta={setDataPlanta}
                          dataPlanta={dataPlanta}
                        />
                      </Collapse>
                    </CardText>
                  </CardBody>
                </Card>
              </Row>
              <Row className="margenChart" style={{display: 'block'}} md={6}>
                <Card style={{ backgroundColor: 'lightgreen' }}>
                  <CardBody>
                    <CardTitle style={{ backgroundColor: 'lightgray' }}>
                      <div
                        onClick={toggleGrafico}
                        style={{ backgroundColor: 'blue' }}
                      >
                        Gráfico
                      </div>
                    </CardTitle>
                    <CardText>
                      <Collapse isOpen={isOpenGrafico}>
                        <Grafico
                          plantaSeleccionada={plantaSeleccionada}
                          espacioSeleccionado={espacioSeleccionado}
                          setDataPlanta={setDataPlanta}
                          dataPlanta={dataPlanta}
                        />
                      </Collapse>
                    </CardText>
                  </CardBody>
                </Card>
              </Row>
            </Col>
          </Container>
        </div>
  )
}

export default Dashboard