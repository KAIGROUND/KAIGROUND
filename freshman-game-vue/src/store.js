import Vuex from 'vuex';
import Vue from "vue";
import createPersistedState from 'vuex-persistedstate'
Vue.use(Vuex)

export const store = new Vuex.Store({
    state: {
        class: null
    },
    mutations: {
        currentUser(state, my_class) {
            state.class = my_class
        }
    },
    plugins: [
        createPersistedState()
    ]
});
