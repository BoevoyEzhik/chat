import axios from "axios";

export default class AuthService {
    static async register() {
        const response = await axios.get('/auth/register')
        return response.data;
    }
}