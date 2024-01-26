import React, { useState } from 'react';
import axios from 'axios';
import Header from './components/Header/Header';
import VideoSection from './components/VideoSection/VideoSection';
import './App.css';
const App = () => {
  return(
    <div className='App'>
      <Header />
      <VideoSection />
    </div>
    
  )
};

export default App;
