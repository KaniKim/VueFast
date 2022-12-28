import {createStore} from "vuex";
import Axios from "@/api/default";

export const store = createStore({
  state: {
    userInfo: null,
    isLogin: false,
  },
  getters: {},
  mutations: {
    loginSuccess(state, payload) {
      state.isLogin = true;
      state.userInfo = payload;
    },
    logout(state) {
      state.isLogin = false;
      state.userInfo = null;
      localStorage.removeItem("accessToken");
      localStorage.removeItem("refreshToken");
    }
  },
  actions: {
    getAccountInfo({commit}) {
      let token = localStorage.getItem("accessToken");
      Axios.get("/api/userinfo", {
        headers: {
          "X-AUTH-TOKEN": token
        }
      })
        .then((res) => {
          commit("loginSucess", res.data.data);
        })
        .catch((err) => {
          console.log(err);
        });
    }
  },
});
