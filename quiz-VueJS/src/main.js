import { createApp } from 'vue'
import App from './App.vue'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    // Définissez vos routes ici
  ]
})

createApp(App).use(router).mount('#App')
