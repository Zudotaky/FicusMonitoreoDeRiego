import React from 'react'
import Planta from './Plant'

let espacios = [{id: 1},{id: 2},{id: 3},{id: 4}];

function ListaDeEspacios(){
    return espacios.map((espacio, index) => {
        return(
         <tr key={espacio.id} ><Planta /> {espacio.id}</tr>
        );
    })
}

export default ListaDeEspacios;