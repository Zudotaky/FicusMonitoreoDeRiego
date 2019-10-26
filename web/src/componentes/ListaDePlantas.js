import React, {useEffect} from 'react'
import Planta from './Plant'
import Servicios from './Servicios';

function ListaDePlantas(props){
    const {plantas, setPlantas, plantaSeleccionada, setPlantaSeleccionada, espacioSeleccionado, setDataPlanta} = props;
   
    useEffect(() => {
        new Servicios().obtenerPlantas(espacioSeleccionado).then(setPlantas);
    }, [espacioSeleccionado]);

    if (!espacioSeleccionado){
        return <span>Seleccione un espacio</span>
    }

    const handleClick = (plantaId) => {
        new Servicios().obtenerDataChart(plantaSeleccionada).then(setDataPlanta);

        setPlantaSeleccionada(plantaId)
    }

    return plantas.map(planta => <tr key={planta.id} >
            <Planta {...planta} 
                handleClick={() => handleClick} 
                selected={planta.id === plantaSeleccionada}  />
        </tr>
    )

    //const plantasArray = plantas.filter((planta, index) => planta.id === id)

    //Aca va el map
}

export default ListaDePlantas;