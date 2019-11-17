import React from 'react'
import { Button } from 'reactstrap'

function ColapseBar(props) {
const { handleClick } = props

return (
<Button 
 color="primary"
 onClick={handleClick} 
 style={{ marginBottom: '1rem', width:'100%'  }}>Espacios</Button>)
}

export default ColapseBar