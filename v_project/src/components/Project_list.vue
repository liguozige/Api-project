<template>
  <div style="height: 100%">
    <el-container style="height: 100%">
      <el-aside width="200px">
        <Menu></Menu>
      </el-aside>

      <el-container>
        <el-header style="background-color: #409eff">

        </el-header>
        <el-main>
          <h1>项目列表页</h1>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import Menu from "@/components/Menu";
export default {
  name: "Project_list",
  components:{
    Menu,
  }
}
</script>

<style scoped>
  .el-header, .el-footer {
    background: linear-gradient(to right, #E0EAFC, #CFDEF3);
    color: #333;
    text-align: center;
    line-height: 0px;
  }

  .el-aside {
    background-color: #D3DCE6;
    color: #333;

  }

  .el-main {
    background-color: white;
    color: #333;
    line-height: 10px;
  }
  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }

  .el-container:nth-child(7) .el-aside {
    line-height: 320px;
  }
</style>