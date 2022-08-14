<template>
  <div style="height: 100%">
    <el-container style="height: 100%">
      <el-aside width="200px">
        <Menu></Menu>
      </el-aside>

      <el-container>
        <el-header style="background-color: #409eff;padding-top: 10px">
           <el-input
              placeholder="请输入项目名称，描述关键字，回车搜索"
              prefix-icon="el-icon-search"
              style="width: 333px"
              v-model="keys"
              @change="change_search">
           </el-input>
        </el-header>
        <el-main>
           <el-table
              :data="project_list_data"
              stripe
              style="width: 100%">
              <el-table-column
                prop="id"
                label="ID"
                width="180">
              </el-table-column>
              <el-table-column
                prop="name"
                label="项目名称"
                width="180">
              </el-table-column>
              <el-table-column
                prop="creater_name"
                label="项目创建者"
                width="180">
              </el-table-column>
              <el-table-column
                prop="des"
                label="描述">
              </el-table-column>

              <el-table-column>
                <template slot="header">
                  <el-button style="width: 121px" @click="Add_project()">新增项目</el-button>
                </template>
                <template slot-scope="scope">
                  <router-link :to ="'/project_detail?project_id='+ scope.row.id"><el-button size="mini" type="primary">进入</el-button></router-link>
                  &nbsp;
                  <el-button size="mini" type="danger" @click="Delete_project(scope.row.id)">删除</el-button>

                </template>
              </el-table-column>
            </el-table>
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
  name: "Project_list",
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
    change_search(){
      axios.get("http://localhost:8000/get_project_list/",{
        params:{
          keys:this.keys
        }
      }).then(res=>{
        this.project_list_data=res.data
      })
    },
    Delete_project(project_id){
      axios.get("http://localhost:8000/delete_project/",{
        params:{
          project_id:project_id
        }
      }).then(res=>{
        this.project_list_data=res.data
      })
    },
    Add_project(){
      axios.get("http://localhost:8000/add_project/").then(res=>{
        this.project_list_data = res.data
      })
    },
  },
  mounted() {
    axios.get("http://localhost:8000/get_project_list/").then(res=>{
      this.project_list_data=res.data
    })
  }
}
</script>

