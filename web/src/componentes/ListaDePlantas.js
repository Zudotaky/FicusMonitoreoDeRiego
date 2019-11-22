import React, {useEffect, Fragment} from 'react'
import Planta from './Plant'
import Servicios from '../servicios/plantasServ'
import '../css/card.css'
import '../css/textInCards.css'

type Props = {
    plantas: string,
    setPlantas: string,
    plantaSeleccionada: string,
    setPlantaSeleccionada: string,
    espacioSeleccionado: string
  }

function ListaDePlantas(props: Props){
    const {plantas, setPlantas, plantaSeleccionada, setPlantaSeleccionada, espacioSeleccionado} = props
   
    useEffect(() => {
        new Servicios().obtenerPlantas(espacioSeleccionado).then(setPlantas)
    },[ espacioSeleccionado])           

    return <Fragment>
     { espacioSeleccionado ?
        plantas.map(planta => 
        <div key={planta.id} >
            <Planta
                {...planta} 
            handleClick={() => setPlantaSeleccionada(planta.id)}
            selected={planta.id === plantaSeleccionada}
            idPlanta={planta.id} />
        </div>) :
        <div className= 'card'>
            <div className="textInCards">
                <h4 className="lineaDebajo"></h4>
                <h4 className="lineaDebajo"><b>Seleccione un espacio</b></h4>
                <p>Una vez seleccionado un espacio podrá ver las plantas que contiene.</p>
            </div>
        </div> 
    } </Fragment>
}

export default ListaDePlantas