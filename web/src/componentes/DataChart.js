import React from 'react'
import {
  AreaChart,
  Area,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer
} from 'recharts'

function generarDataHumedad(rawData) {
  return {
    name: rawData.fecha,
    uv: calcularNivelDeHumedad(rawData.humedad),
    pv: 0,
    amt: 0
  }
}

function calcularNivelDeHumedad(humedad) {
  // Seco, Mojado, Muy mojado.
  if (humedad < 300) {
    return 'Seco'
  }
  if (humedad < 600) {
    return 'Mojado'
  }
  return 'Muy mojado'
}

type Props = {
  dataPlanta: string
}

export default function DataChart(props: Props) {
  const { dataPlanta } = props
  const dataProcesada = (dataPlanta.Registros || []).map(senso =>
    generarDataHumedad(senso)
  )
  return (
    <ResponsiveContainer width="99%" height={500}>
      <AreaChart
        data={dataProcesada}
        margin={{
          top: 20,
          right: 30,
          left: 10,
          bottom: 10
        }}
      >
        <CartesianGrid strokeDasharray="4 4" />
        <XAxis tick={{ fill: 'yellow', fontWeight: 'bold' }} dataKey="name" />
        <YAxis tick={{ fill: 'yellow', fontWeight: 'bold' }} type="category" />
        <Tooltip />
        <Area type="monotone" dataKey="uv" stroke="#8884d8" fill="#8884d8" />
      </AreaChart>
    </ResponsiveContainer>
  )
}
