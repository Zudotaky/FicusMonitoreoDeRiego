import React, { useState, useCallback} from 'react'
import {
    Collapse,
    CardBody,
    Card,
    CardTitle
  } from 'reactstrap'

import '../css/card.css'

function ColapsableSection({ title, children }) {
    const [isOpen, setIsOpen] = useState(false)
    const toggleIsOpen = useCallback(() => {
      setIsOpen(o => !o)
    }, [])
  
    return (
      <Card className='colapsableBackground'>
        <CardBody>
          <CardTitle>
            <div onClick={toggleIsOpen} className='colapsableText'>
              {title}
            </div>
          </CardTitle>
          <Collapse isOpen={isOpen}>{children}</Collapse>
        </CardBody>
      </Card>
    )
  }
  
  export default ColapsableSection