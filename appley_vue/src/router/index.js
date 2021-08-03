import { createRouter, createWebHistory } from 'vue-router'
import Home from '../components/Home.vue'
import Users from '../components/User.vue'
import Fruits from '../components/Fruits.vue'
import UserEdit from '../components/UserEdit.vue'
import UserRegister from '../components/UserRegister.vue'
import FruitsCreate from '../components/FruitsCreate.vue'
import FruitEdit from '../components/FruitEdit.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/users',
    name: 'Users',
    component: Users
  },
  {
    path: '/register',
    name: 'UserRegister',
    component: UserRegister
  },
  {
    path: '/edituser/:id',
    name: 'UserEdit',
    component: UserEdit
  },
  {
    path: '/fruits',
    name: 'Fruits',
    component: Fruits
  },
  {
    path: '/create',
    name: 'FruitsCreate',
    component: FruitsCreate
  },
  {
    path: '/editfruit/:id',
    name: 'FruitEdit',
    component: FruitEdit
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
