import React, { PureComponent } from 'react';
import {
  AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip,
} from 'recharts';

const data = [
  {
    name: 'Fecha A', uv: 1023, pv: 0, amt: 0,
  },
  {
    name: 'Fecha B', uv: 200, pv: 0, amt: 0,
  },
  {
    name: 'Fecha C', uv: 290, pv: 0, amt: 0,
  },
  {
    name: 'Fecha D', uv: 400, pv: 0, amt: 0,
  },
  {
    name: 'Fecha E', uv: 358, pv: 4800, amt: 2181,
  },
  {
    name: 'Fecha F', uv: 190, pv: 3800, amt: 2500,
  },
  {
    name: 'Fecha G', uv: 502, pv: 4300, amt: 2100,
  },
];

export default class DataChart extends PureComponent {
  static jsfiddleUrl = 'https://jsfiddle.net/alidingling/Lrffmzfc/';

  render() {
    return (
      <AreaChart
        width={600}
        height={400}
        data={data}
        margin={{
          top: 10, right: 30, left: 0, bottom: 0,
        }}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Area type="monotone" dataKey="uv" stroke="#8884d8" fill="#8884d8" />
      </AreaChart>
    );
  }
}