import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Project_list from "@/components/Project_list";
import Project_detail from "@/components/Project_detail";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path:'/project_list',
      component:Project_list
    },
    {
      path:'/project_detail',
      component:Project_detail
    }
  ]
})
