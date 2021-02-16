import Vue from 'vue'
import App from './components/App.vue'
import vuetify from './plugins/vuetify';
import VueRouter from 'vue-router';
import Login from "./components/Login";
import Main from "./components/Main";
import { store } from "./store";

Vue.config.productionTip = false
Vue.use(VueRouter)


const router = new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/login',
      component: Login,
    },
    {
      path: '/',
      component: App,
      meta: {authRequired: true}
    }
  ],
});

router.beforeEach((to, from, next) => {
  if(!store.state.class && to.matched.some((info)=>info.meta.authRequired)) next('/login')
  else next();
  if(store.state.class) next('/')
  else next();
})
new Vue({
  router,
  vuetify,
  store,
  render: h => h(Main)
}).$mount('#app')
