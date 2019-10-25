import React, {useEffect} from 'react'
import Planta from './Plant'
import Servicios from './Servicios';


function ListaDePlantas(props){
    const {plantas, setPlantas, plantaSeleccionada, setPlantaSeleccionada, espacioSeleccionado, setDataPlanta} = props;

    if (espacioSeleccionado){
        new Servicios().obtenerPlantas(espacioSeleccionado).then(setPlantas);
    } else {
        return <span>Seleccione un espacio</span>
    }

    const clickHandler = (idPlanta) => {

            new Servicios().obtenerDataChart(idPlanta).then(console.log);

    }

    return plantas.map(planta => <tr key={planta.id} >
            <Planta {...planta} 
                handleClick={() => clickHandler(planta.id)} 
                selected={planta.id === plantaSeleccionada}  />
        </tr>
    )

    //const plantasArray = plantas.filter((planta, index) => planta.id === id)

    //Aca va el map
}

export default ListaDePlantas;