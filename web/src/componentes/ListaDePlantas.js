import React, {useEffect} from 'react'
import Planta from './Plant'
import Servicios from '../servicios/plantasServ'


function ListaDePlantas(props){
    const {plantas, setPlantas, plantaSeleccionada, setPlantaSeleccionada, espacioSeleccionado} = props
   
    useEffect(() => {
        new Servicios().obtenerPlantas(espacioSeleccionado).then(setPlantas)
    }, [espacioSeleccionado])

    if (!espacioSeleccionado){
        return <span>Seleccione un espacio</span>
    }               

    return plantas.map(planta => 
        <tr key={planta.id} >
            <Planta
                {...planta} 
               handleClick={() => setPlantaSeleccionada(planta.id)}
               selected={planta.id === plantaSeleccionada}
               idPlanta={planta.id} />
        </tr>
    )
}

export default ListaDePlantas