import React from 'react';
import axios from 'axios';

function App() {

  async function testGetReq() {
    const response = await axios.get('/auth/register')
    console.log(response.data)
  }

  return (
    <div className="App">
      <button onClick={testGetReq}>
        get
      </button>
    </div>
  );
}

export default App;
