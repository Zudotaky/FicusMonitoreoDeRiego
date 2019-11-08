import React, {Component} from 'react'
import Planta from './Plant'
import Servicios from './Servicios'
import '../css/card.css'
import '../css/textInCards.css'

function Espacio(props){
        const {id} = props
        const {nombre} = props
        const {descripcion} = props
        const {imagen} = props

        return(
            <div className="card" onClick={props.handleClick} /*style={props.selected ? "backgroundColor: red": ""}*/>
                <img className="card-img-top" src={imagen} alt="Imagen de espacio no disponible."/>
                    <div className="textInCards">
                        <h4 className="lineaDebajo"><b>{nombre}</b></h4>
                        <p>{descripcion}</p>
                    </div>
            </div>
        )
    }


export default Espacio;