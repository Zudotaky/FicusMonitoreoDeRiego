import React from 'react'
import Planta from './Plant'

let plantas = [{id: 1},{id: 2},{id: 3},{id: 4}];

function ListaDePlantas(){
    return plantas.map((planta, index) => {
        return(
         <tr key={planta.id} ><Planta /> {planta.id}</tr>
        );
    })
}

export default ListaDePlantas;