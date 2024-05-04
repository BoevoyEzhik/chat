import React, { useEffect, useState } from 'react';
import cl from './AuthForm.module.css'
import AuthHeader from '../AuthHeader/AuthHeader.jsx';
import AuthInput from '../AuthInput/AuthInput.jsx';
import AuthButton from '../AuthButton/AuthButton.jsx';
import { useFetching } from '../../../../hooks/useFetching.js';
import AuthService from '../../../../API/AuthService.js';

const AuthForm = () => {

    const [originalPassword, setOriginalPassword] = useState('')
    const [maskedPassword, setMaskedPassword] = useState('')
    const [password2, setPassword2] = useState({})
    const [isPassRight, setPassRight] = useState(true)
    const [login, setLogin] = useState('')
    const [email, setEmail] = useState('')
    const [isLogin, setIsLogin] = useState(true)
    const [fetchRegister, isRegisterLoading, registerError] = useFetching(async () => {
        const isRegisterOk = await AuthService.register();
        setIsLogin(!isLogin)
        console.log(isRegisterOk.data)
    })

    const [fetchLogin, isLoginLoading, loginError] = useFetching(async () => {
        const isLoginOk = await AuthService.login(login, originalPassword);
        setIsLogin(isLogin)
        console.log(isLoginOk.data)
    })

    // useEffect(() => {   
    //     console.log('Effect orig ' + originalPassword)
    //     console.log('Effect mask ' + maskedPassword)
    // }, [originalPassword, maskedPassword])

    const handlePassword = (text) => {
        if (!originalPassword) {
            setOriginalPassword(text)
        } else {
            originalPassword.length < text.length ? setOriginalPassword(originalPassword + text[text.length-1]) : setOriginalPassword(originalPassword.slice(0, originalPassword.length-1)) 
        }
        setMaskedPassword(maskText(text))
    }

    const maskText = (text) => {
        return text.replaceAll(/./g, '*')
    }

    const register = (e) => {
        e.preventDefault();
        setIsLogin(!isLogin)
    }

    const checkLogin = (e) => {
        e.preventDefault();
        console.log("Orig pass " + originalPassword)
        console.log("mask pass " + maskedPassword)
    }

    const tryToLogin = event => {
        event.preventDefault()
        AuthService.login(login, originalPassword)
    }

    const loginWithPrevent = (e, ...args) => {
        console.log('@@@args ' + JSON.stringify(args))
        e.preventDefault();
        fetchLogin(...args)
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
                            value={maskedPassword}
                            onChange={e => handlePassword(e.target.value)}
                        />
                        {!isPassRight ? <span>Пароль должен содержать 4 символа или больше'</span> : ''} 
                        </>
                    : <><AuthInput
                            type='text'
                            text='Логин'
                            value={login}
                            onChange={e => setLogin(e.target.value)}
                        />
                        <AuthInput
                            type='text'
                            text='Пароль'
                            value={maskedPassword}
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
                            value={email}
                            onChange={e => setEmail(e.target.value)}
                        /></>}
                <AuthButton onClick={isLogin ? (e) => loginWithPrevent(e, login, originalPassword) : (e) => fetchRegister(e)}>
                    {isLogin ? 'ВОЙТИ' : 'ЗАРЕГИСТРИРОВАТЬСЯ'}
                </AuthButton>
            </form>
            {isLogin ? <AuthButton onClick={e => register(e)}>РЕГИСТРАЦИЯ
             </AuthButton>: null}
             
            
        </div>
        
        
    );
};

export default AuthForm;