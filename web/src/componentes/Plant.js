import React from 'react'

const imageStyle = {
    width: '100%',
};

function calcularEstado(humedad){
    // Exceso de riego, Riego estable, Falta riego
    if(humedad<300){
        return <font size="2" color="red">Falta riego.</font>;
    }
    if(humedad<600){
        return <font size="2" color="Green">Riego estable.</font>;
    }
    return <font size="2" color="Blue">Exceso de riego.</font>;
}

function Plant(props){
    console.log(props)
    return(
        <div className="card" onClick={() => props.handleClick(props.id)}>
            <img className="card-img-top" src={props.imagen} alt="Imagen de Planta no disponible."/>
            <h4 className="lineaDebajo"><b>{props.nombre}</b></h4>
            <p>Estado de la planta: {calcularEstado(900)}</p>
            <h4 className="lineaDebajo"></h4>
            <p>{props.descripcion}</p>
        </div>
    )
}

export default Plant;