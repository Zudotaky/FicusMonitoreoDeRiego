import React, { useState, useEffect } from 'react'
import { Carousel, CarouselItem, CarouselControl, CarouselIndicators, CarouselCaption
} from 'reactstrap'
import espaciosServ from '../servicios/espaciosServ'

import '../css/listaCartas.css'
import '../css/carruselImagen.css'

type Props = {
  espacios: string,
  setEspacios: string,
  espacioSeleccionado: string,
  setEspacioSeleccionado: string
}

function Carrusel(props: Props) {
  
  const [activeIndex, setActiveIndex] = useState(0)
  const [animating, setAnimating] = useState(false)
  const { espacios, setEspacios, espacioSeleccionado, setEspacioSeleccionado, setNombreEspacio} = props


  const next = () => {
    if (animating) return
    const nextIndex = activeIndex === espacios.length - 1 ? 0 : activeIndex + 1
    setActiveIndex(nextIndex)
  }

  const previous = () => {
    if (animating) return
    const nextIndex = activeIndex === 0 ? espacios.length - 1 : activeIndex - 1
    setActiveIndex(nextIndex)
  }

  const goToIndex = (newIndex) => {
    if (animating) return
    setActiveIndex(newIndex)
  }

  useEffect(() => {
    new espaciosServ().obtenerEspacios().then(setEspacios)
  }, [])

  const onSelect = (id, nombre) => {
      setEspacioSeleccionado(id)
      setNombreEspacio(nombre)
  }

  const slides = espacios.map((item) => {
    let carruselImagenClass = 'carruselImagen' 
    if (espacioSeleccionado === item.id) {
      carruselImagenClass += ' tarjetaSeleccionada'
    }
    return (
      <CarouselItem
        className="custom-tag"
        tag="div"
        key={item.id}
        onExiting={() => setAnimating(true)}
        onExited={() => setAnimating(false)}
      >
        <img className={carruselImagenClass} src={item.imagen} alt={item.altText} onClick= {()=>onSelect(item.id,item.nombre)}/>
        <CarouselCaption className="letrasCarrito" captionText={ item.nombre } captionHeader={item.descripcion} />
      </CarouselItem>
    )
  })

  return (
    <div>
      <Carousel className='carrito'
        activeIndex={activeIndex}
        next={next}
        previous={previous}
        interval={false}
      >
        <CarouselIndicators items={espacios} activeIndex={activeIndex} onClickHandler={goToIndex} />
        {slides}
        <CarouselControl direction="prev" directionText="Previous" onClickHandler={previous} />
        <CarouselControl direction="next" directionText="Next" onClickHandler={next} />
      </Carousel>
    </div>
  )
}

export default Carrusel
