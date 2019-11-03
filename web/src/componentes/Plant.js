/* eslint-disable react/prop-types */
import React from 'react'
import Servicios from './Servicios'

// const imageStyle = {
//     width: '100%',
// }

function calcularEstado(humedad){
    // Exceso de riego, Riego estable, Falta riego
    if(humedad<300){
        return <font size="2" color="red">Falta riego.</font>
    }
    if(humedad<600){
        return <font size="2" color="Green">Riego estable.</font>
    }
    return <font size="2" color="Blue">Exceso de riego.</font>
}

const handleClick = (plantaId) => {
    new Servicios().obtenerDataChart(plantaId).then((planta) => {
        console.log(planta)
    })
    // setPlantaSeleccionada(plantaId)
}

function Plant(props){
    return(
        <div className="card" onClick={() => handleClick(props.id)}>
            <img className="card-img-top" src={props.imagen} alt="Imagen de Planta no disponible."/>
            <h4 className="lineaDebajo"><b>{props.nombre}</b></h4>
            <p>Estado de la planta: {calcularEstado(900)}</p>
            <h4 className="lineaDebajo"></h4>
            <p>{props.descripcion}</p>
        </div>
    )
}

export default Plant