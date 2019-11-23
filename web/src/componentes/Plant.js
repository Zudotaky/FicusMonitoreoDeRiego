import React, {useEffect, useState} from 'react'
import EstadoHumedad from './EstadoHumedad'
import Servicios from '../servicios/registrosServ'
import '../css/card.css'
import '../css/textInCards.css'

type Props = {
    selected: string,
    idPlanta: string,
    imagen: string,
    handleClick: string,
    descripcion: string,
    nombre: string
    }

function Plant(props: Props){
    const {selected, idPlanta} = props
    const [ultimoSenso, setUltimoSenso] = useState({})

   useEffect(() => {
        new Servicios().obtenerUltimoSenso(idPlanta).then(setUltimoSenso)
    }, [selected])

   let className = 'card'
   if (selected) {
     className += ' tarjetaSeleccionada'
   }
    const imageBackground = {
        backgroundImage: 'url(' + props.imagen + ')'
    }

    return(
        <div className={ className } onClick={props.handleClick}>
            <div className='loadingCard'>
                <div className="card-img-top" src={props.imagen} style={imageBackground} alt="Imagen de Planta no disponible."/>
            </div>
            <div className="textInCards">
                <h4 className="lineaDebajo"><b>{props.nombre}</b></h4>
                <p>Estado de la planta: <EstadoHumedad humedad={ultimoSenso.humedad}/></p>
                <h4 className="lineaDebajo"></h4>
                <p>{props.descripcion}</p>
            </div>
        </div>
    )
}

export default Plant