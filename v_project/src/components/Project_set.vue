<template>
  <div>
    <el-form ref="form" :model="form_data" label-width="80px">
      <el-form-item label="项目名称">
        <el-input v-model="form_data.name"></el-input>
      </el-form-item>

      <el-form-item label="项目描述">
        <el-input v-model="form_data.des"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="Save_project">保存生效</el-button>
      </el-form-item>

    </el-form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Project_set",
  data(){
    return{
      form_data:{
        name:'',
        des:'',
      },
    }
  },
  methods:{
    Save_project(){
      axios.post('http://localhost:8000/save_project/',this.form_data).then(
        this.$message({
          message:"保存成功",
          type:'success',
      }))
    }
  },
  mounted:function () {
    axios.get("http://localhost:8000/get_project_detail/",{
      params:{
        id:this.project_id
      }
    }).then(res=>{
      this.form_data=res.data
    })
  },
  props:["project_id"]
}
</script>

<style scoped>

</style>