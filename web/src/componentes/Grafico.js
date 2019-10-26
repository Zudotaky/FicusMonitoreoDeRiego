import React, { useState, useEffect } from "react";
import Servicios from "./Servicios";
import DataChart from "./DataChart"

function Grafico(props) {
  const {plantaSeleccionada, setDataPlanta, dataPlanta} = props;

  useEffect(() => {
    new Servicios().obtenerDataChart(plantaSeleccionada).then(setDataPlanta);
  }, [plantaSeleccionada]);

  if (!plantaSeleccionada) {
    return <span>Grafico</span>
  }

  return (
    <DataChart dataPlanta={dataPlanta} />
  )
}

export default Grafico;