import { React, useState, useEffect } from 'react';
import { Line } from 'react-chartjs-2';



const Apple = () => {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
  
    useEffect(() => {
      fetch('/api/apple')
        .then((response) => {
          if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
          }
          return response.json();
        })
        .then((data) => {
          setData(data);
          setLoading(false);
        })
        .catch((error) => {
          setError(error);
          setLoading(false);
        });
    }, []);
  
    if (loading) {
      return <div>Loading...</div>;
    }
  
    if (error) {
      return <div>Error: {error.message}</div>;
    }
  
    // Here, you can add your chart rendering logic based on the data fetched.
    return (
      <div>
        <h1>Apple Data</h1>
        <p>Chart will go here...</p>
      </div>
    );
};

export default Apple;
