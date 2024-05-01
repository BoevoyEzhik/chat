import React from 'react';
import axios from 'axios';
import './styles/App.css'
import AuthInput from './components/UI/auth/AuthInput/AuthInput.jsx';
import AuthButton from './components/UI/auth/AuthButton/AuthButton.jsx';
import AuthHeader from './components/UI/auth/AuthHeader/AuthHeader.jsx';
import AuthForm from './components/UI/auth/AuthForm/AuthForm.jsx';

function App() {

  async function testGetReq() {
    const response = await axios.get('/auth/register')
    console.log(response.data)
  }

  return (
    <div className="App">
      <AuthForm/>
    </div>
  );
}

export default App;
