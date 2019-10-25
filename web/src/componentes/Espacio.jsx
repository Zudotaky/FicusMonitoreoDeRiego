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

        return(
  //          <div onClick={()=>handleClick(id)}>
            <div className="card">
                <img className="card-img-top" src={'https://cdn.homedit.com/wp-content/uploads/2016/08/DIY-pipe-plant-stand-300x250.jpg'} alt="PlantImage"/>
                <h4 className="lineaDebajo"><b>{nombre}</b></h4>
                <p>{descripcion}</p>
                {id}
            </div>
        )
    }
}

export default Espacio;