import { createRouter, createWebHistory,createWebHashHistory } from 'vue-router'
import App from '../App.vue'
import HelloWorld from '../components/HelloWorld.vue'
import LawPrediction from '../components/LawPrediction.vue'
import ProductFunction from '../components/ProductFunction.vue'
import LawColumn from '../components/LawColumn.vue'
import AVue from '@/views/A.vue'
import BVue from '@/views/B.vue'
import CaseSearchVue from '@/components/CaseSearch.vue'
import CaseView from '@/components/CaseView.vue'

const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    {
      path: '/',
      redirect: '/lp' // 重定向到你想要的默认路由，比如 LawPrediction 组件
    },
    {
      path: '/a',
      name: 'App',
      component: AVue
    },
    {
      path: '/b',
      name: 'HelloWorld',
      component: BVue
    },
    {
      path: '/lp',
      name: 'lp',
      component: LawPrediction
    },
    {
      path: '/pf',
      name: 'pf',
      component: ProductFunction
    },
    {
      path: '/lc',
      name: 'lc',
      component: LawColumn
    },
    {
      path:'/cv',
      name:'caseView',
      component:CaseView
    },
    {
      path:'/caseView/:param',
      name:'caseView1',
      component:CaseView
    }
  ]
})

export default router
