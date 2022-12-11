import axios from 'axios';

const instance = axios.create({
  withCredentials: true,
  baseURL: 'http://127.0.0.1:5000/',
  headers: {'Content-Type':'application/x-www-form-urlencoded'}
});

export default instance;