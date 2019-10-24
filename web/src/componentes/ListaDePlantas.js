import React from 'react'
import Planta from './Plant'

let plantas = [{id: 1},{id: 2},{id: 3},{id: 4}];

function ListaDePlantas(){
    return plantas.map((planta, index) => {
        return(
         <tr key={planta.id} ><Planta /> {planta.id}</tr>
        );
    })

    //const plantasArray = plantas.filter((planta, index) => planta.id === id)

    //Aca va el map
}

export default ListaDePlantas;