import React from 'react'

type Props = {
    humedad: number,
    }

function EstadoHumedad (props: Props) {
    const {humedad} = props
    // Exceso de riego, Riego estable, Falta riego
    if(humedad<300){
        return <font size="2" color="red">Falta riego.</font>
    }
    if(humedad<600){
        return <font size="2" color="Green">Riego estable.</font>
    }
    return <font size="2" color="Blue">Exceso de riego.</font>
}

export default EstadoHumedad