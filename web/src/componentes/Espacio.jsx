import React, {Component} from 'react'
import Servicios from '../servicios/espaciosServ'
import '../css/card.css'
import '../css/textInCards.css'
import '../css/tarjetaSeleccionada.css'
import {
    Carousel,
    CarouselItem,
    CarouselControl,
    CarouselIndicators,
    CarouselCaption
  } from 'reactstrap';
  


function Espacio(props){
        const {id} = props
        const {nombre} = props
        const {descripcion} = props
        const {imagen} = props
        const {selected} = props

        let className = 'card'
        if (selected) {
          className += ' tarjetaSeleccionada'
        }

        return(
                <div className={className} onClick={props.handleClick} /*style={props.selected ? "backgroundColor: red": ""}*/>
                    <img className="card-img-top" src={imagen} alt="Imagen de espacio no disponible."/>
                        <div className="textInCards">
                            <h4 className="lineaDebajo"><b>{nombre}</b></h4>
                            <p>{descripcion}</p>
                        </div>
                </div>
        )
    }

export default Espacio