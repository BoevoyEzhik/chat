import React from 'react';
import cl from './AuthHeader.module.css'

const AuthHeader = () => {
    return (
        <div className={cl.authHeader}>
            {/* <img src='./logo.svg' alt='logo' className={cl.logo}/> */}
            <span className={cl.authHeader__text}>Войти в чат</span>
        </div>
    );
};

export default AuthHeader;