import Vuex from 'vuex';
import Vue from "vue";
import createPersistedState from 'vuex-persistedstate'
Vue.use(Vuex)

export const store = new Vuex.Store({
    state: {
        class: null,
        pw: null
    },
    mutations: {
        currentUser(state, my_class) {
            state.class = my_class
        },
        currentPw(state, my_pw){
            state.pw = my_pw
        }
    },
    plugins: [
        createPersistedState()
    ]
});
