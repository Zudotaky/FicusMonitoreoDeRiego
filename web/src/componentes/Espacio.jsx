import React, {Component} from 'react'
import Planta from './Plant'
import Servicios from './Servicios';

class Espacio extends Component{

    // handleClick = (id) => {
    //     this.props.selectEspacio(id)
    // }

    render(){
        const {id} = this.props

        return(
  //          <div onClick={()=>handleClick(id)}>
            <div>
                {id}
            </div>
        )
    }
}

export default Espacio;