import React, {useEffect, useState} from 'react'
import Servicios from '../servicios/registrosServ'
import '../css/card.css'
import '../css/textInCards.css'

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

function Plant(props){
    const {selected, idPlanta} = props
    const [ultimoSenso, setUltimoSenso] = useState({})

   useEffect(() => {
        new Servicios().obtenerUltimoSenso(idPlanta).then(setUltimoSenso)
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
                <p>Estado de la planta: {calcularEstado(ultimoSenso.humedad)}</p>
                <h4 className="lineaDebajo"></h4>
                <p>{props.descripcion}</p>
            </div>
        </div>
    )
}

export default Plant