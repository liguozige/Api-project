<template>
    <el-menu
      :default-openeds="['1','2']"
      :default-active="da"
      router
      class="el-menu-vertical-demo"
      @open="handleOpen"
      @close="handleClose"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b">
      <el-menu-item index="/">首页Home</el-menu-item>
      <el-submenu index="1">
        <template slot="title">
          <i class="el-icon-menu"></i>
          <span>功能区</span>

        </template>
          <el-menu-item index="/project_list/">项目管理</el-menu-item>
          <el-menu-item index="1-2">环境管理</el-menu-item>
          <el-menu-item index="1-3">官方接口库</el-menu-item>
          <el-menu-item index="1-4">线上监控</el-menu-item>
        <el-menu-item-group>
          <template slot="title">接口导入</template>
          <el-menu-item index="1-5">接口文档</el-menu-item>
          <el-menu-item index="1-6">Postman</el-menu-item>
          <el-menu-item index="1-7">在线抓包</el-menu-item>
          <el-menu-item index="1-8">其他</el-menu-item>
        </el-menu-item-group>
      </el-submenu>

      <el-submenu index="2">
        <template slot="title">
          <i class="el-icon-user-solid"></i>
          <span>用户区</span>
        </template>
          <el-menu-item index="2-1">个人资料</el-menu-item>
          <el-menu-item index="2-2">个人贡献</el-menu-item>
          <el-menu-item index="2-3">发送消息</el-menu-item>
          <a href="http://localhost:8000/help/"><el-menu-item>帮助</el-menu-item></a>
          <a href="http://localhost:8000/logout/"><el-menu-item>退出</el-menu-item></a>
      </el-submenu>

      <el-submenu index="3">
        <template slot="title">
          <i class="el-icon-s-tools"></i>
          <span>维护区</span>
        </template>
          <el-menu-item index="3-1">进入后台</el-menu-item>
          <el-menu-item index="3-2">用户管理</el-menu-item>
          <el-menu-item index="3-3">查看日志</el-menu-item>
          <el-menu-item index="3-4">发布公告</el-menu-item>
      </el-submenu>


    </el-menu>
</template>

<script>
export default {
  name: "Menu",
  data(){
    return{
      da:window.location.hash.split('#')[1].split('?')[0],
    }
  },
  methods: {
      handleOpen(key, keyPath) {
        console.log(key, keyPath);
      },
      handleClose(key, keyPath) {
        console.log(key, keyPath);
      }
    }
}
</script>

<style scoped>

</style>