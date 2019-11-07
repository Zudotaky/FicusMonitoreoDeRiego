import React, {Component} from 'react'
import Planta from './Plant'
import Servicios from './Servicios'
import '../css/card.css'

function Espacio(props){
        const {id} = props
        const {nombre} = props
        const {descripcion} = props
        const {imagen} = props

        return(
            <div className="card" onClick={props.handleClick} /*style={props.selected ? "backgroundColor: red": ""}*/>
                <img className="card-img-top" src={imagen} alt="Imagen de espacio no disponible."/>
                <h4 className="lineaDebajo"><b>{nombre}</b></h4>
                <p>{descripcion}</p>
                {id}
            </div>
        )
    }


export default Espacio;