import axios from "axios";

const Axios = axios.create({
  baseURL: import.meta.env.VITE_APP_BASE_API
});

Axios.defaults.timeout = 2500;

Axios.interceptors.request.use(
  config => {
    return config;
  },
  error => {
    console.log(error);
    return Promise.reject(error);
  }
);

Axios.interceptors.response.use(
  response => {
    const res = response.data;
    return res;
  },
  error => {
    console.log(error);
    return Promise.reject(error);
  }
);

export default Axios;

