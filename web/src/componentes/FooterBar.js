import React from "react";
import {Container, Row, Col} from 'reactstrap'
import '../css/bar.css'

function Footer() {
  return (
    <div className="footer">  
            <Row>
              <Col className='footerRow' md={3}>
                <h1>asdfgh asdqwer</h1>
              </Col>
              <Col className='footerRow' md={3}>
                <h1>asdfgh asdqwer</h1>
              </Col>
              <Col className='footerRow' md={5}>
                  <a href='https://github.com/Zudotaky/FicusMonitoreoDeRiego/wiki'>about us</a>
              </Col>
            </Row>
      </div>
  )
}

export default Footer