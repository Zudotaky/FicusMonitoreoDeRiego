import React, { useEffect } from 'react'
import Espacio from './Espacio'
import Servicios from '../servicios/espaciosServ'

function ListaDeEspacios(props) {
  const {espacios, setEspacios, espacioSeleccionado, setEspacioSeleccionado} = props

  useEffect(() => {
    new Servicios().obtenerEspacios().then(setEspacios)
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
