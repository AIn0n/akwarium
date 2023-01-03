import "bootstrap/dist/css/bootstrap.css"
import "bootstrap/dist/js/bootstrap.js"
import { createApp } from 'vue'
import App from './App.vue'
import router from "./router"

import './assets/main.css'
import { createPinia } from 'pinia'

createApp(App).use(createPinia()).use(router).mount('#app')
