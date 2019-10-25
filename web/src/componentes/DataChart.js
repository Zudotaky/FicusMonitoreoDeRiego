import React, { PureComponent } from 'react';
import {
  AreaChart, Area, XAxis, YAxis, CartesianGrid, Tooltip,
} from 'recharts';
import Servicios from './Servicios'


/*const data = [
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
];*/


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

export default class DataChart extends PureComponent {
  static jsfiddleUrl = 'https://jsfiddle.net/alidingling/Lrffmzfc/';

  render() {
    if (this.props.dataPlanta){
      const data = this.props.dataPlanta.map( datos => {
        datos.name = datos.fecha
        datos.uv = datos.humedad
      })

      return (
        <AreaChart
          width={700}
          height={500}
          data={data}
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
      );
    } else { 
      return <div> asd </div>
    }
  } 
}