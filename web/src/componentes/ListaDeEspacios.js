import React, { useState, useEffect } from "react";
import Espacio from "./Espacio";
import Servicios from "./Servicios";

function ListaDeEspacios() {
  const [espacios, setEspacios] = useState([]);

  useEffect(() => {
    new Servicios().obtenerEspacios().then(setEspacios);
  }, []);
  
  return espacios.map(espacio => (
    <tr key={espacio.id}>
      <Espacio {...espacio} />
    </tr>
  ));

  //const plantasArray = plantas.filter((planta, index) => planta.id === id)

  //Aca va el map
}

export default ListaDeEspacios;
