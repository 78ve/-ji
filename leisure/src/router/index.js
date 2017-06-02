import Vue from 'vue'
import Router from 'vue-router'

//components
import Login from '@/components/Login'
import Home from '@/components/Home'
import Leisure from '@/components/Leisure'
import Cart from '@/components/Cart'
import Order from '@/components/Order'
import Admin from '@/components/Admin'
import UserInfo from '@/components/UserInfo'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/',
      name: 'Leisure',
      component: Leisure,
      children: [
        {
          path: '',
          component: Home
        },
        {
          path: 'cart',
          component: Cart
        },
        {
          path: 'order',
          component: Order
        },
        {
          path: 'userinfo',
          component: UserInfo
        },
        {
          path: 'admin',
          component: Admin
        }
      ]
    }
  ]
})
