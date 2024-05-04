import axios from "axios";

export default class AuthService {
    static async register() {
        const response = await axios.get('/auth/register')
        return response;
    }

    // static async login(login, password) {
    //     const response = await axios.post('http://localhost:8000/auth/login', {"email": login, "password": password})
            
 
    //     console.log(response)
    // }

    static async login(...args) {
        const [login, password] = args
        console.log("args!!!! " + args)
        console.log("login " + typeof(login))
        console.log("password " + password)
        const response = await fetch('http://localhost:8000/auth/login', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'WithCredentials': false,
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json; charset=UTF-8',
                'Access-Control-Allow-Methods': 'OPTIONS,GET,POST,PUT,DELETE',
                'Access-Control-Allow-Headers': 'Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With',
                'Authorization': ''
            },
            mode: "no-cors",
            body: JSON.stringify({'email': login, 'password': password})
        })

        const result = await response.json()
        console.log(result)
    }

    // static async login (login, password) {
    //     const options = {
    //         method: 'POST',
    //         mode: 'no-cors',
    //         headers: {
    //             'Accept': 'application/json',
    //             'WithCredentials': false,
    //             'Access-Control-Allow-Origin': '*',
    //             'Content-Type': 'application/json; charset=UTF-8',
    //             'Access-Control-Allow-Methods': 'OPTIONS,GET,POST,PUT,DELETE',
    //             'Access-Control-Allow-Headers': 'Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With',
    //             'Authorization': ''
    //         },
    //         data: {
    //             "email": login,
    //             password
    //         },
    //         url: 'http://localhost:8000/auth/login'
    //     }
    //     const response = await axios(options)
    //     console.log(response)
    // }
}