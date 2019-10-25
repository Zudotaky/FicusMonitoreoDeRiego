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
    return(
        <div className="card" onClick={() => props.handleClick}>
            <img className="card-img-top" src={'https://cdn.homedit.com/wp-content/uploads/2016/08/DIY-pipe-plant-stand-300x250.jpg'} alt="PlantImage"/>
            <h4 className="lineaDebajo"><b>{props.nombre}</b></h4>
            <p>Estado de la planta: {calcularEstado(900)}</p>
        </div>
    )
}

export default Plant;