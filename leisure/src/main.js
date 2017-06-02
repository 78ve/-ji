// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './vuex/store'

import axios from 'axios';

import iView from 'iview';
import 'iview/dist/styles/iview.css';
import '../theme/index.less';

import Crypto from 'crypto-js'
import Icon from 'vue-svg-icon/Icon.vue';
import VueParticles from 'vue-particles'
import VueLocalStorage from 'vue-ls';



let options = {
  namespace: 'vuejs__'
};

Vue.use(VueLocalStorage, options);

require('vue2-animate/dist/vue2-animate.min.css')
var TWEEN = require('tween.js');

Vue.config.productionTip = false

Vue.use(iView);
Vue.component('icon', Icon);
Vue.use(VueParticles);


Vue.prototype.$request = axios
Vue.prototype.$Crypto = Crypto

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { 
  	App
   }
})
