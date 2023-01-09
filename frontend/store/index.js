import Vuex from "vuex";
import axios from "axios";
import Axios from "../api/default";

export default new Vuex.Store({
  state: {
    user: null,
    access_token: null,
    refresh_token: null,
  },
  mutations: {
    SET_USER_DATA(state, userData) {
      state.user = userData.email;
      state.access_token = userData.access_token;
      state.refresh_toekn = userData.refresh_token;
      axios.defaults.headers.common["Authorization"] = `Bearer ${userData.access_token}`;
    },
    SET_REFRESH_TOKEN(state, userData) {
      state.access_token = userData.access_token;
      state.refresh_token = userData.refresh_token;
    },
    REMOVE_TOKEN(state) {
      state.access_token = null;
      state.refresh_token = null;
    }
  },
  actions: {
    login({commit}, credentials) {
      return Axios.post("/auth/login", credentials).then(
        (res) => {
          commit("SET_USER_DATA", res);
        });
    },
    refresh_token({commit}) {
      return new Promise((resolve, reject) => {
        Axios.post("/auth/certify")
          .then(res => {
            commit("SET_REFRESH_TOKEN", res);
          })
          .catch(err => {
            console.log("refreshToken error : ", err.config);
          });
      });
    },
    logout({commit}) {
      commit("REMOVE_TOKEN");
    }
  }
});

