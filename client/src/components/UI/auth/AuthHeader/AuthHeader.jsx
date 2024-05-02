import React from 'react';
import cl from './AuthHeader.module.css'

const AuthHeader = () => {

    const logoUrl = ''

    return (
        <div className={cl.authHeader}>
            {/* <img src={logoUrl} alt='logo' className={cl.logo}/> */}
            <span className={cl.authHeader__text}>Войти в чат</span>
        </div>
    );
};

export default AuthHeader;