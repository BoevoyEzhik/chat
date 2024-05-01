import React from 'react';
import cl from './AuthInput.module.css';

const AuthInput = (props) => {
    return (
        // <fieldset className={cl.authInputForm}>
        //     <legend className={cl.authInputText}>{props.text}</legend>
        //     <input className={cl.authInput} {...props}/>
        // </fieldset>
        <div className={cl.authInputForm}>
            <input id='input' className={cl.authInputField} {...props}>              
            </input>
            <label htmlFor='input' className={cl.authInputLabel}>
                <span style={{boxSizing: 'inherit'}}>{props.text}</span>
            </label>
        </div>
    );
};

export default AuthInput;