import React, { PureComponent, useEffect } from 'react'
import { AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip} from 'recharts'
import Servicios from './Servicios'


const dataABCHardCoded = [
  {
    name: getCurrentDateFormated(), uv: "Seco", pv: 0, amt: 0,
  },
  {
    name: getCurrentDateFormated(), uv: "Mojado", pv: 0, amt: 0,
  },
  {
    name: getCurrentDateFormated(), uv: "Muy mojado", pv: 0, amt: 0,
  },
  {
    name: getCurrentDateFormated(), uv: "Muy mojado", pv: 0, amt: 0,
  },
  {
    name: getCurrentDateFormated(), uv: "Mojado", pv: 0, amt: 0,
  },
  {
    name: getCurrentDateFormated(), uv: "Mojado", pv: 0, amt: 0,
  },
  {
    name: getCurrentDateFormated(), uv: "Mojado", pv: 0, amt: 0,
  },
  {
    name: getCurrentDateFormated(), uv: "Mojado", pv: 0, amt: 0,
  },
  {
    name: getCurrentDateFormated(), uv: "Muy mojado", pv: 0, amt: 0,
  },
  {
    name: getCurrentDateFormated(), uv: "Muy mojado", pv: 0, amt: 0,
  },
  {
    name: getCurrentDateFormated(), uv: "Seco", pv: 0, amt: 0,
  },
];


function getCurrentDateFormated() {

    var today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth() + 1; //Enero era 0!
    var yyyy = today.getFullYear();
    if (dd < 10) {
      dd = '0' + dd;
    } 
    if (mm < 10) {
      mm = '0' + mm;
    } 
    var today = dd + '/' + mm + '/' + yyyy;
    //TODO cambiar esto return today;
    return "10:25:32 01/02/1993";
  }

  function generarDataHumedad(rawData){
    return {
              name: rawData.fecha,
              uv: calcularNivelDeHumedad(rawData.humedad),
              pv: 0,
              amt: 0,
            }
  }
  
  function calcularNivelDeHumedad(humedad){
    // Seco, Mojado, Muy mojado.
    if(humedad<300){
        return 'Seco'
    }
    if(humedad<600){
        return 'Mojado'
    }
    return 'Muy mojado'
  }

export default function DataChart(props) {
  const jsfiddleUrl = 'https://jsfiddle.net/alidingling/Lrffmzfc/';
    const {dataPlanta} = props
    let dataProcesada = []
    dataPlanta.Registros.map(senso => dataProcesada.push(generarDataHumedad(senso)))
    console.log('dataProcesada',dataProcesada)
    return (
      <AreaChart
        width={700}
        height={500}
        data={dataProcesada ? dataProcesada : []}
        margin={{
          top: 20, right: 30, left: 10, bottom: 10,
        }}
        >
        <CartesianGrid strokeDasharray="4 4" />
        <XAxis dataKey="name" />
        <YAxis type="category" />
        <Tooltip />
        <Area type="monotone" dataKey="uv" stroke="#8884d8" fill="#8884d8" />
      </AreaChart>
    )
  }




///////////////Registros y medida de humedad.
/*
let xs = {
  registros:[
    {
      fecha: "2019-10-26 09:38:51",
      temperatura: 0,
      humedad: 100,
      plantaId: 1
    }
  ]
}
let data = []
data.push()

///Linea que genera la data
dataPlanta.registros.map(senso => data.push(generarDataHumedad(senso)))


function generarDataHumedad(rawData){
  return {
            name: rawData.fecha,
            UV: calcularNivelDeHumedad(rawData.humedad),
            pv: 0,
            amt: 0,
          }
}

function calcularNivelDeHumedad(humedad){
  // Seco, Mojado, Muy mojado.
  if(humedad<300){
      return 'Seco'
  }
  if(humedad<600){
      return 'Mojado'
  }
  return 'Muy mojado'
}
  */