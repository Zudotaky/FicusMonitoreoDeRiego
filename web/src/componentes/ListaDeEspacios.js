import React from 'react'
import Planta from './Plant'
import Servicios from './Servicios';

function ListaDeEspacios(){
    let serv = new Servicios()
    let espacios = serv.obtenerEspacios()
    console.log("espacios")
    console.log(espacios)
    console.log("espaciosaaaaaaassssssaaaaaaaaaaaa")
    console.log(espacios.then(response => {return response.json();}));
    return(
        'pepepe'
    )
    // return espacios.then(espacio, index) => {
    //     return(
    //      <tr key={espacio['id']} > {espacio['id']} {espacio['nombre']} </tr>
    //     );
    // })
}

// completed: false
// id: 1​
// title: "delectus aut autem"
// userId: 1

export default ListaDeEspacios;