import React, { useState, useCallback} from 'react'
import {
    Collapse,
    CardBody,
    Card,
    CardTitle
  } from 'reactstrap'

function ColapsableSection({ title, children }) {
    const [isOpen, setIsOpen] = useState(false)
    const toggleIsOpen = useCallback(() => {
      setIsOpen(o => !o)
    }, [])
  
    return (
      <Card style={{ backgroundColor: 'lightgreen' }}>
        <CardBody>
          <CardTitle style={{ backgroundColor: 'lightgray' }}>
            <div onClick={toggleIsOpen} style={{ backgroundColor: 'blue' }}>
              {title}
            </div>
          </CardTitle>
          <Collapse isOpen={isOpen}>{children}</Collapse>
        </CardBody>
      </Card>
    )
  }
  
  export default ColapsableSection