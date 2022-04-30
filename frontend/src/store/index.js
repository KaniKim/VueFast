import { createStore } from "vuex";
import axios from "axios";
import qs from "qs";
import Cookies from "js-cookie";

export default createStore({
  state: {
    user: localStorage.getItem("username") || null,
    access_token: localStorage.getItem("access_token") || null,
    refresh_token: localStorage.getItem("refresh_token") || null,
  },
  getters: {},
  mutations: {
    setUser(state, user) {
      state.user = user;
    },
    setAccessToken(state, access_token) {
      state.access_token = access_token;
    },
    setRefreshToken(state, refresh_token) {
      state.refresh_token = refresh_token;
    },
  },
  actions: {
    LOGIN({ commit }, userData) {
      const config = {
        headers: { "content-type": "application/x-www-form-urlencoded" },
      };
      axios
        .post("http://localhost:8000/auth", qs.stringify({ userData }), config)
        .then((res) => {
          commit("setUser", res.data.username);
          Cookies.set("access_token", res.data.access_token, "15m");
          Cookies.set("refresh_token", res.data.refresh_token, "30d");
          commit("setAccessToken", res.data.access_token);
          commit("setRefreshToken", res.data.refresh_token);
          return res;
        });
    },
  },
  modules: {},
});
