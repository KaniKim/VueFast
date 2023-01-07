import Vuex from "vuex";
import axios from "axios";

export default new Vuex.Store({
  state: {
    user: null
  },
  mutations: {
    SET_USER_DATA(state, userData) {
      state.user = userData;
      localStorage.setItem("user", JSON.stringify(userData));
      axios.defaults.headers.common["Authorization"] = `Bearer ${userData.access_token}`;
    }
  },
  actions: {
    register({commit}, credentials) {
      return axios.post("//localhost:8000/auth/login/", credentials).then(
        ({data}) => {
          commit("SET_USER_DATA", data);
        });
    }
  }
});

