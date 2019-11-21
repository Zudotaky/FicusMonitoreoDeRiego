import React, { useState, Children, useEffect } from 'react'
import {
  Carousel,
  CarouselItem,
  CarouselControl,
  CarouselIndicators,
  CarouselCaption
} from 'reactstrap'

import espaciosServ from '../servicios/espaciosServ'

import '../css/listaCartas.css'
import '../css/carruselImagen.css'

const items = [
  {
    id: 1,
    altText: '',
    caption: 'Slide 1'
  },
  {
    id: 2,
    altText: 'Slide 2',
    caption: 'Slide 2'
  },
  {
    id: 3,
    altText: 'Slide 3',
    caption: 'Slide 3'
  }
]

function Carrusel(props) {
  //console.log(props.children.props)
  

  const [activeIndex, setActiveIndex] = useState(0)
  const [animating, setAnimating] = useState(false)
  const {espacios, setEspacios, espacioSeleccionado, setEspacioSeleccionado} = props


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

//Children.map(children, (child)=> <CarouselItem>{child}</CarouselItem>)


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
        <img className={carruselImagenClass} src={item.imagen} alt={item.altText} onClick= {()=>setEspacioSeleccionado(item.id)}/>
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
