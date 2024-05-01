import React, { useState } from 'react';
import cl from './AuthForm.module.css'
import AuthHeader from '../AuthHeader/AuthHeader.jsx';
import AuthInput from '../AuthInput/AuthInput.jsx';
import AuthButton from '../AuthButton/AuthButton.jsx';

const AuthForm = () => {

    const [password, setPassword] = useState('')
    const [password2, setPassword2] = useState('')
    const [login, setLogin] = useState('')
    const [email, setEmail] = useState('')
    const [isLogin, setIsLogin] = useState(true)

    const maskText = (text) => {
        return text.replaceAll(/./g, '*')
    }

    const register = (e) => {
        e.preventDefault()
        setIsLogin(!isLogin)
    }

    return (
        <div className={cl.authForm}>
            <form className={cl.authForm}>
                <AuthHeader/>
                {isLogin 
                    ? <><AuthInput
                            type='text'
                            text='Почта или логин'
                            value={login}
                            onChange={e => setLogin(e.target.value)}
                        />
                        <AuthInput
                            type='text'
                            text='Пароль'
                            value={password}
                            onChange={e => setPassword(maskText(e.target.value))}
                        /></> 
                    : <><AuthInput
                            type='text'
                            text='Логин'
                            value={login}
                            onChange={e => setLogin(e.target.value)}
                        />
                        <AuthInput
                            type='text'
                            text='Пароль'
                            value={password}
                            onChange={e => setPassword(maskText(e.target.value))}
                        /><AuthInput
                            type='text'
                            text='Подтверждение пароля'
                            value={password2}
                            onChange={e => setPassword2(maskText(e.target.value))}
                        />
                        <AuthInput
                            type='text'
                            text='E-mail'
                            value={login}
                            onChange={e => setEmail(e.target.value)}
                        /></>}
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