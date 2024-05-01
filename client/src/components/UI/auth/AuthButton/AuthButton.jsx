import React from 'react';
import cl from './AuthButton.module.css'

const AuthButton = ({children, ...props}) => {
    return (
        <button {...props} className={cl.authButton}>
            {children}
        </button>
    );
};

export default AuthButton;