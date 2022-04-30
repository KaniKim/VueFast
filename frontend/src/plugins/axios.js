import axios from "axios";
import Cookies from "js-cookie";
import { refreshToken } from "@/plugins/login";

const AxiosInst = axios.create();

AxiosInst.interceptors.request.use(
  async function (config) {
    config.headers.authorization = Cookies.get("access_token");
    config.headers.refresh = Cookies.get("refresh_token");
    return config;
  },
  (err) => {
    return Promise.reject(err);
  }
);

AxiosInst.interceptors.response.use(
  (res) => {
    return res;
  },
  async (err) => {
    console.log(err.response);
    if (err.response.status === 400) {
      await refreshToken();
    }
    return Promise.reject(err);
  }
);

export default AxiosInst;
