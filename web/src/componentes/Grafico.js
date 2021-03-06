import React, { useEffect, Fragment} from 'react'
import RegistrosServ from '../servicios/registrosServ'
import DataChart from './DataChart'

type Props = {
  setDataPlanta: string,
  dataPlanta: string,
  espacioSeleccionado: string,
  plantaSeleccionada: string
}

function Grafico(props: Props) {
  const {plantaSeleccionada, espacioSeleccionado, setDataPlanta, dataPlanta} = props

  useEffect(() => {
    new RegistrosServ().obtenerDataChart(plantaSeleccionada).then(setDataPlanta)
  }, [plantaSeleccionada])

  if(!espacioSeleccionado){
    return <Fragment></Fragment>
  }
  if (espacioSeleccionado && !plantaSeleccionada) {
    return <div className= 'card'>
    <div className="textInCards">
        <h4 className="lineaDebajo"></h4>
        <h4 className="lineaDebajo"><b>Seleccione una planta</b></h4>
        <p>Una vez seleccionada una planta podrá ver sus registros historicos.</p>
    </div>
</div>
  }
  return (
    <DataChart dataPlanta={dataPlanta} />
  )
}

export default Grafico