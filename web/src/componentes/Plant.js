/* eslint-disable react/prop-types */
import React, {useEffect} from 'react'
import Servicios from './Servicios'
import DataChart from './DataChart'
import '../css/card.css'
import '../css/textInCards.css'
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

// const obtenerDataPlanta = (plantaId, props) => {
//     let dataPlanta= null
//     new Servicios().obtenerDataChart(plantaId).then((registros) => {
//         dataPlanta = registros
//         props.plantaSeleccionada = plantaId
//     })
//     console.log('planta seleccionada')
//     console.log(props.plantaSeleccionada)
//     return dataPlanta
// }

function Plant(props){
    const {selected, idPlanta} = props
    let ultimoSenso = {}

   useEffect(() => {
        new Servicios().obtenerUltimoSenso(idPlanta).then((senso)=>{ultimoSenso = senso})
        console.log('ultimoSenso', ultimoSenso)
    }, [selected])



   let className = 'card'
   if (selected) {
     className += ' tarjetaSeleccionada'
   }
    
    return(
        <div className={ className } onClick={props.handleClick}>
            <img className="card-img-top" src={props.imagen} alt="Imagen de Planta no disponible."/>
            <div className="textInCards">
                <h4 className="lineaDebajo"><b>{props.nombre}</b></h4>
                <p>Estado de la planta: {calcularEstado(900)}</p>
                <h4 className="lineaDebajo"></h4>
                <p>{props.descripcion}</p>
            </div>
        </div>
    )
}

export default Plant