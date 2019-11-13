import React, { useEffect } from 'react'
import Espacio from './Espacio'
import espaciosServ from '../servicios/espaciosServ'

function ListaDeEspacios(props) {
  const {espacios, setEspacios, espacioSeleccionado, setEspacioSeleccionado} = props

  useEffect(() => {
    new espaciosServ().obtenerEspacios().then(setEspacios)
  }, [])

  return espacios.map(espacio => (
      <Espacio key={espacio.id}
        {...espacio} 
        handleClick={() => setEspacioSeleccionado(espacio.id)} 
        selected={espacio.id === espacioSeleccionado} 
      />
  ))
}

export default ListaDeEspacios
