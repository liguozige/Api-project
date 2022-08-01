<template>
  <div id="home" style="height: 100%">
    <el-container style="height: 100%;">
      <el-aside width="200px">
        <Menu></Menu>
      </el-aside>
      <el-container>
        <el-header height="70px">
          <el-row :gutter="5">
            <el-col :span="6">
              <div class="staticbanner" style="background-color: #409eff">
                <div class="title">
                  <p>官方接口: {{ real_time_datas.ApiShop_count }}</p>
                  <el-tag size="mini" style="color: #409eff">实时</el-tag>
                </div>
              </div>
            </el-col>

            <el-col :span="6">
              <div class="staticbanner" style="background-color: #67c23a">
                <div class="title">
                  <p>官方接口: {{ real_time_datas.UnReadNews_count }}</p>
                  <el-tag size="mini" style="color: #67c23a">实时</el-tag>
                </div>
              </div>
            </el-col>

            <el-col :span="6">
              <div class="staticbanner" style="background-color: #e6a23c">
                <div class="title">
                  <p>官方接口: {{ real_time_datas.RunCase_count }}</p>
                  <el-tag size="mini" style="color: #e6a23c">实时</el-tag>
                </div>
              </div>
            </el-col>

            <el-col :span="6">
              <div class="staticbanner" style="background-color: #9299a1">
                <div class="title">
                  <p>官方接口: {{ real_time_datas.Import_count }}</p>
                  <el-tag size="mini" style="color: #9299a1">实时</el-tag>
                </div>
              </div>
            </el-col>
          </el-row>
        </el-header>
        <el-main style="padding-bottom: 1px;">
          <el-card class="box-card" style="width: 30%;float: left;margin-right: 3px;">
            <div slot="header" class="clearfix">
              <span>项目总览</span>
            </div>
            <p>项目总数:{{ tj_datas.overview.project_count }}</p>
            <p>接口总数:{{ tj_datas.overview.api_count }}</p>
            <p>用例总数:{{tj_datas.overview.case_count}}</p>
            <p>环境总数:{{tj_datas.overview.env_count}}</p>
            <p>用户总数:{{tj_datas.overview.user_count}}</p>
          </el-card>
          <el-card class="box-card" style="width: -webkit-calc(70% - 20px);float: left;">
            <div slot="header" class="clearfix">
              <span>上次监控情况</span>
            </div>
            <span style="font-size: xx-small">用例通过率</span>
            <el-progress style="margin-bottom: 10px" :text-inside="true" :stroke-width="15" :percentage="tj_datas.monitor.case_pass"></el-progress>
            <span style="font-size: xx-small">接口通过率</span>
            <el-progress style="margin-bottom: 10px"  :text-inside="true" :stroke-width="15" :percentage="tj_datas.monitor.api_pass" status="success"></el-progress>
            <span style="font-size: xx-small">用例失败率</span>
            <el-progress style="margin-bottom: 10px"  :text-inside="true" :stroke-width="15" :percentage="tj_datas.monitor.case_fail" status="warning"></el-progress>

          </el-card>
          <el-card class="box-card" style="width: -webkit-calc(70% - 20px);float: left;">
            <div slot="header" class="clearfix">
              <span>个人贡献</span>
            </div>
            <table class="table">
              <thead>
              <tr>
                <th>个人项目占比</th>
                <th>个人用例占比</th>
                <th>个人接口占比</th>
                <th>监控贡献占比</th>
                <th>执行用例占比</th>
              </tr>

              </thead>
              <tbody>
              <tr>
                <td><el-progress type="circle" :percentage="tj_datas.contribution.project" color="#67c23a" style="margin-right: 25px;margin-left: 20px"></el-progress></td>
                <td><el-progress type="circle" :percentage="tj_datas.contribution.case" color="#ff4949" style="margin-right: 25px"></el-progress></td>
                <td><el-progress type="circle" :percentage="tj_datas.contribution.api" style="margin-right: 25px"></el-progress></td>
                <td><el-progress type="circle" :percentage="tj_datas.contribution.monitor" color="#e6a23c" style="margin-right: 25px"></el-progress></td>
                <td><el-progress type="circle" :percentage="tj_datas.contribution.case_run"></el-progress></td>
              </tr>
              </tbody>
            </table>
          </el-card>
          <el-card class="box-card" style="overflow-y: auto; width: 30%;float: left;margin-left: 3px;">
            <div slot="header" class="clearfix">
              <span>待处理消息</span>
              <el-button style="float: right; padding: 3px 0" type="text">查看更多</el-button>
            </div>
            <div v-for="o in tj_datas.news" class="text item">
              {{'消息: '+o.content}}
            </div>
          </el-card>
        </el-main>
        <el-footer style="min-height: 110px;padding-top: 15px;text-align: left;">
          <el-card class="box-card" style="overflow-y: auto;line-height: 5px;padding:5px;width: 100%;min-height: 80%;">
            <div v-for="o in tj_datas.notices" class="text item"  style="color: red;">
              {{'平台更新日志: ' + o.content }}
            </div>
          </el-card>
        </el-footer>
      </el-container>
    </el-container>
  </div>
</template>

<script>
// @ is an alias to /src
import Menu from "../components/Menu.vue"
import axios from 'axios'
export default {
  name:'home',
  data(){
    return{
      tj_datas:{
        notices:[],
        news:[],
        overview:{
          project_count:0,
          api_count:0,
          case_count:0,
          env_count:0,
          user_count:0
        },
        monitor:{
          case_pass:0,
          api_pass:0,
          case_fail:0
        },
        contribution:{
          project:0,
          case:0,
          api:0,
          monitor:0,
          case_run:0,
        },
      },
      real_time_datas:{
        ApiShop_count:0,
        UnReadNews_count:0,
        RunCase_count:0,
        Import_count:0,
      },
    }
  },
  components:{
    Menu,
  },
  mounted:function (){
    axios('http://localhost:8000/get_tj_datas/').then(res=>{
      this.tj_datas=res.data
    })
    axios.get('http://localhost:8000/get_real_time_datas/').then(res=>{
        this.real_time_datas=res.data
      })
    setInterval(()=>{
        axios.get('http://localhost:8000/get_real_time_datas/').then(res=>{
        this.real_time_datas=res.data
      })
    },100000)
  }
}
</script>

<style>
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
    background-color: #E9EEF3;
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

  .text {
    font-size: 14px;
  }

  .item {
    margin-bottom: 18px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }

  .box-card {
    max-height: 48%;
    min-height: 48%;
  }
  .el-card{
    background-color: white;
    text-align: left;
    overflow-y: auto;

  }
  th,td{
    text-align: center;
    font-size: xx-small;
  }
  .staticbanner{
    color: white;
    height: 50px;
    border-radius: 3px;
    padding: 10px 10px;
  }
  .title{
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  p{
    font-size: 13px;
    font-weight: bold;
  }
</style>