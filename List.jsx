import React from 'react';

const List = ({ places, type, setType, rating, setRating }) => {
  return (
    <div className="bg-white p-6 rounded-lg shadow-md h-full overflow-y-auto">
      <h2 className="text-2xl font-bold mb-4">Find your Companion</h2>
      
      <div className="flex gap-4 mb-6">
        <div className="flex-1">
          <label className="block text-sm font-medium text-gray-700">Type</label>
          <select value={type} onChange={(e) => setType(e.target.value)} className="mt-1 block w-full border-gray-300 rounded-md shadow-sm border p-2">
            <option value="restaurants">Restaurants</option>
            <option value="hotels">Hotels</option>
            <option value="attractions">Attractions</option>
          </select>
        </div>
        
        <div className="flex-1">
          <label className="block text-sm font-medium text-gray-700">Rating</label>
          <select value={rating} onChange={(e) => setRating(e.target.value)} className="mt-1 block w-full border-gray-300 rounded-md shadow-sm border p-2">
            <option value={0}>All</option>
            <option value={3}>Above 3.0</option>
            <option value={4}>Above 4.0</option>
            <option value={4.5}>Above 4.5</option>
          </select>
        </div>
      </div>

      <div className="space-y-4">
        {/* Example Place Card */}
        <div className="border rounded-lg overflow-hidden shadow-sm hover:shadow-md transition">
          <img src="https://via.placeholder.com/300x150" alt="place" className="w-full h-32 object-cover" />
          <div className="p-3">
            <h3 className="font-bold">The Grand Plaza</h3>
            <p className="text-sm text-gray-500">⭐ 4.5 • $$$ • Hotel</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default List;