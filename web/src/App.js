import React from 'react';
import HeaderBar from './componentes/HeaderBar';
import Footer from './componentes/FooterBar';
import 'bootstrap/dist/css/bootstrap.css';
import './css/listaCartas.css';
import './css/margenChart.css';
import './App.css';
import Dashboard from './Dashboard';

function App() {
  return (
    <div className="App">    
        <HeaderBar />
        <Dashboard />
        <Footer />
    </div>
  )
}

export default App