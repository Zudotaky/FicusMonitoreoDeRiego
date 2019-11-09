import React from 'react'
import {Row, Col} from 'reactstrap'
import '../css/bar.css'

function Footer() {
  return (
    <div className="footer">  
            <Row>
              <Col className='footerRow' md={3}>
                <h1>Desarrollado por:</h1>
              </Col>
              <Col className='footerRow' md={3}>
                <h1> Julian Rybczuk </h1>
                <h1> Patricio Otel </h1>
              </Col>
              <Col className='footerRow' md={5}>
                  <a href='https://github.com/Zudotaky/FicusMonitoreoDeRiego/wiki'>Ficus wiki.</a>
              </Col>
            </Row>
      </div>
  )
}

export default Footer