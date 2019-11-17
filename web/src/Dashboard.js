import React, { useState, useCallback, Children } from "react";
import ListaDePlantas from "./componentes/ListaDePlantas";
import ListaDeEspacios from "./componentes/ListaDeEspacios";
import {
  Container,
  Row,
  Col,
  Collapse,
  CardBody,
  Card,
  CardText,
  CardTitle
} from "reactstrap";
import Grafico from "./componentes/Grafico";

function Dashboard() {
  const [espacios, setEspacios] = useState([]);
  const [plantas, setPlantas] = useState([]);
  const [espacioSeleccionado, setEspacioSeleccionado] = useState(null);
  const [plantaSeleccionada, setPlantaSeleccionada] = useState(null);
  const [dataPlanta, setDataPlanta] = useState({});

  return (
      <Container fluid>
        <Col>
          <Row className="listaCartas">
            <CollapsableSection title="Espacios">
              <ListaDeEspacios
                handleClick
                espacios={espacios}
                setEspacios={setEspacios}
                espacioSeleccionado={espacioSeleccionado}
                setEspacioSeleccionado={setEspacioSeleccionado}
              />
            </CollapsableSection>
          </Row>
          <Row className="listaCartas">
            <CollapsableSection title="Plantas">
              <ListaDePlantas
                plantas={plantas}
                setPlantas={setPlantas}
                espacioSeleccionado={espacioSeleccionado}
                plantaSeleccionada={plantaSeleccionada}
                setPlantaSeleccionada={setPlantaSeleccionada}
                setDataPlanta={setDataPlanta}
                dataPlanta={dataPlanta}
              />
            </CollapsableSection>
          </Row>
          <Row className="margenChart" style={{ display: "block"}}>
            <CollapsableSection title="Gráfico">
              <Grafico
                plantaSeleccionada={plantaSeleccionada}
                espacioSeleccionado={espacioSeleccionado}
                setDataPlanta={setDataPlanta}
                dataPlanta={dataPlanta}
              />
            </CollapsableSection>
          </Row>
        </Col>
      </Container>
  );
}

export default Dashboard;

function CollapsableSection({ title, children }) {
  const [isOpen, setIsOpen] = useState(false);
  const toggleIsOpen = useCallback(() => {
    setIsOpen(o => !o);
  }, []);

  return (
    <Card style={{ backgroundColor: "lightgreen" }}>
      <CardBody>
        <CardTitle style={{ backgroundColor: "lightgray" }}>
          <div onClick={toggleIsOpen} style={{ backgroundColor: "blue" }}>
            {title}
          </div>
        </CardTitle>
        <Collapse isOpen={isOpen}>{children}</Collapse>
      </CardBody>
    </Card>
  );
}
