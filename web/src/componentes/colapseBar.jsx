import React from 'react'
import { Button } from 'reactstrap'

type Props = {
  handleClick: string
}

function ColapseBar(props: Props) {
const { handleClick } = props

return (
<Button 
 color="primary"
 onClick={handleClick} 
 style={{ marginBottom: '1rem', width:'100%'  }}>Espacios</Button>)
}

export default ColapseBar