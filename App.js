import React, { useState, useEffect } from 'react';
import Header from './components/Header';
import List from './components/List';
import Map from './components/Map';

const App = () => {
  const [places, setPlaces] = useState([]);
  const [type, setType] = useState('restaurants');
  const [rating, setRating] = useState('');

  return (
    <div className="min-h-screen bg-gray-100">
      <Header />
      <div className="flex flex-col md:flex-row w-full p-4 gap-4">
        <div className="w-full md:w-1/3">
          <List 
            places={places} 
            type={type} 
            setType={setType} 
            rating={rating} 
            setRating={setRating} 
          />
        </div>
        <div className="w-full md:w-2/3 h-[80vh]">
          <Map />
        </div>
      </div>
    </div>
  );
};

export default App;
