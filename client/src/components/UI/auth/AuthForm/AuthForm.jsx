import React, { useState } from 'react';
import cl from './AuthForm.module.css'
import AuthHeader from '../AuthHeader/AuthHeader.jsx';
import AuthInput from '../AuthInput/AuthInput.jsx';
import AuthButton from '../AuthButton/AuthButton.jsx';

const AuthForm = () => {

    const [password, setPassword] = useState('')
    const [login, setLogin] = useState('')
    const [isLogin, setIsLogin] = useState(true)

    const maskText = (text) => {
        return text.replaceAll(/./g, '*')
    }

    const register = (e) => {
        e.preventDefault()
        setIsLogin(false)
    }

    return (
        <div className={cl.authForm}>
            <form className={cl.authForm}>
                <AuthHeader/>
                <AuthInput
                    type='text'
                    text='Имя пользователя'
                    value={login}
                    onChange={e => setLogin(e.target.value)}
                />
                <AuthInput
                    type='text'
                    text='Пароль'
                    value={password}
                    onChange={e => setPassword(maskText(e.target.value))}
                />
                <AuthButton onClick={(e) => e.preventDefault()}>
                    {isLogin ? 'ВОЙТИ' : 'ЗАРЕГИСТРИРОВАТЬСЯ'}
                </AuthButton>
            </form>
             <AuthButton onClick={(e) => register(e)}>{isLogin ? 'РЕГИСТРАЦИЯ' : 'ВОЙТИ'}
             </AuthButton>
            
        </div>
        
        
    );
};

export default AuthForm;