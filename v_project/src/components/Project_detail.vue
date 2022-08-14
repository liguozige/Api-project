<template>
  <div style="height: 100%">
    <el-container style="height: 100%">
      <el-aside width="200px">
        <Menu></Menu>
      </el-aside>

      <el-container>
        <el-header style="line-height: 60px;background-color: white;padding-top: 10px">
          <span style="float: right;" >项目ID:{{$route.query.project_id}}</span>
        </el-header>
        <el-main>
          <h1>项目详情页</h1>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

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

<script>
import Menu from "@/components/Menu";
import axios from "axios";
export default {
  name: "Project_detail",
  data(){
    return{
      keys:'',
      project_list_data:[],
    }
  },
  components:{
    Menu,
  },
  methods:{

  },
  mounted() {

  }
}
</script>

