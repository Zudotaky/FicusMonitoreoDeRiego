import React, {Component} from 'react'
import Planta from './Plant'
import Servicios from './Servicios';

class Espacio extends Component{

    // handleClick = (id) => {
    //     this.props.selectEspacio(id)
    // }

    render(){
        const {id} = this.props
        const {nombre} = this.props
        const {descripcion} = this.props
        const {imagen} = this.props

        return(
  //          <div onClick={()=>handleClick(id)}>
            <div className="card" onClick={this.props.handleClick} /*style={props.selected ? "backgroundColor: red": ""}*/>
                <img className="card-img-top" src={imagen} alt="Imagen de espacio no disponible."/>
                <h4 className="lineaDebajo"><b>{nombre}</b></h4>
                <p>{descripcion}</p>
                {id}
            </div>
        )
    }
}

export default Espacio;