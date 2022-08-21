<template>
  <div style="height: 100%">
    <el-container style="height: 100%">
      <el-aside width="200px">
        <Menu></Menu>
      </el-aside>
        <el-main>
          <span style="float: right;" >项目ID:{{$route.query.project_id}}</span>
          <el-tabs v-model="tab_name">
            <el-tab-pane label="项目设置" name="first">
              <Project_set :project_id="$route.query.project_id"></Project_set>
            </el-tab-pane>
            <el-tab-pane label="用例管理" name="second">
              <Project_case></Project_case>
            </el-tab-pane>
          </el-tabs>

        </el-main>
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
    line-height: 30px;
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
import Project_case from "@/components/Project_case";
import Project_set from "@/components/Project_set";
export default {
  name: "Project_detail",
  data(){
    return{
      keys:'',
      project_list_data:[],
      tab_name:'first',
    }
  },
  components:{
    Menu,
    Project_case,
    Project_set,
  },
  methods:{

  },
  mounted() {

  }
}
</script>

