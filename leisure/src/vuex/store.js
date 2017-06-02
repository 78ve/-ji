import Vue  from 'vue';
import Vuex from 'vuex';
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    username: '',
    password: '',
    user_id:0,
    popularbooks: [],
    popularbooks_len:0,
    newestbooks:[],
    newestbooks_len:0

  },
  mutations: {
    Set_UserInfo(state, userinfo) {
      state.username = userinfo.username;
      state.password = userinfo.password;
    },
    Set_UserID(state, user) {
      state.user_id = user.user_id;
    },
    Set_PolularBooks(state, books) {
      state.popularbooks = books.info;
      state.popularbooks_len = books.len;
    },
    Set_NewBooks(state, books) {
      state.newestbooks = books.info;
      state.newestbooks_len = books.len;
    },
  },
  actions: {
    SET_USER_INFO({commit}, userinfo) {
      commit('Set_UserInfo', userinfo);
    },
    SET_USER_ID({commit}, user) {
      commit('Set_UserID', user);
    },
    FETCH_POPULAR_BOOKS(context){
      axios({
        method: 'put',
        url: '/api/book?type=popular'
      }).then((response) => { 

       
        context.commit('Set_PolularBooks', response.data);
      })
    },
    FETCH_NEW_BOOKS(context){
      axios({
        method: 'put',
        url: '/api/book?type=newest'
      }).then((response) => { 
        
        context.commit('Set_NewBooks', response.data);
      })
    }
  },
  getters: {
    getUsername: (state) => state.username,
    getUserID: (state) => state.user_id,
    getPopularBooks: (state) => state.popularbooks,
    getPopularLen: (state) => state.popularbooks_len,
    getNewbooks: (state) => state.newestbooks,
    getNewbooksLen: (state) => state.newestbooks_len,
  }
})