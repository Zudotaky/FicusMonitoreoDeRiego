import React from 'react'
import '../css/card.css'
import '../css/textInCards.css'
import '../css/tarjetaSeleccionada.css'

  
type Props = {
  nombre: string,
  descripcion: string,
  imagen: string,
  selected: string,
  handleClick: string
}

function Espacio(props: Props){
        const {nombre} = props
        const {descripcion} = props
        const {imagen} = props
        const {selected} = props

        let className = 'card'
        if (selected) {
          className += ' tarjetaSeleccionada'
        }

        return(
                <div className={className} onClick={props.handleClick}>
                    <img className="card-img-top" src={imagen} alt="Imagen de espacio no disponible."/>
                        <div className="textInCards">
                            <h4 className="lineaDebajo"><b>{nombre}</b></h4>
                            <p>{descripcion}</p>
                        </div>
                </div>
        )
    }

export default Espacio

/*style={props.selected ? "backgroundColor: red": ""}*/