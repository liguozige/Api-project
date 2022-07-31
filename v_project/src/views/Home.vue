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
                  <p>官方接口: 19</p>
                  <el-tag size="mini" style="color: #409eff">实时</el-tag>
                </div>
              </div>
            </el-col>

            <el-col :span="6">
              <div class="staticbanner" style="background-color: #67c23a">
                <div class="title">
                  <p>官方接口: 19</p>
                  <el-tag size="mini" style="color: #67c23a">实时</el-tag>
                </div>
              </div>
            </el-col>

            <el-col :span="6">
              <div class="staticbanner" style="background-color: #e6a23c">
                <div class="title">
                  <p>官方接口: 19</p>
                  <el-tag size="mini" style="color: #e6a23c">实时</el-tag>
                </div>
              </div>
            </el-col>

            <el-col :span="6">
              <div class="staticbanner" style="background-color: #9299a1">
                <div class="title">
                  <p>官方接口: 19</p>
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
            <p>项目总数</p>
            <p>接口总数</p>
            <p>用例总数</p>
            <p>环境总数</p>
            <p>用户总数</p>
          </el-card>
          <el-card class="box-card" style="width: -webkit-calc(70% - 20px);float: left;">
            <div slot="header" class="clearfix">
              <span>上次监控情况</span>
            </div>
            <span style="font-size: xx-small">用例通过率</span>
            <el-progress style="margin-bottom: 10px" :text-inside="true" :stroke-width="15" :percentage="70"></el-progress>
            <span style="font-size: xx-small">接口通过率</span>
            <el-progress style="margin-bottom: 10px"  :text-inside="true" :stroke-width="15" :percentage="100" status="success"></el-progress>
            <span style="font-size: xx-small">用例失败率</span>
            <el-progress style="margin-bottom: 10px"  :text-inside="true" :stroke-width="15" :percentage="80" status="warning"></el-progress>

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
                <td><el-progress type="circle" :percentage="25" color="#67c23a" style="margin-right: 25px;margin-left: 20px"></el-progress></td>
                <td><el-progress type="circle" :percentage="25" color="#ff4949" style="margin-right: 25px"></el-progress></td>
                <td><el-progress type="circle" :percentage="25" style="margin-right: 25px"></el-progress></td>
                <td><el-progress type="circle" :percentage="25" color="#e6a23c" style="margin-right: 25px"></el-progress></td>
                <td><el-progress type="circle" :percentage="25"></el-progress></td>
              </tr>
              </tbody>
            </table>
          </el-card>
          <el-card class="box-card" style="overflow-y: auto; width: 30%;float: left;margin-left: 3px;">
            <div slot="header" class="clearfix">
              <span>待处理消息</span>
              <el-button style="float: right; padding: 3px 0" type="text">查看更多</el-button>
            </div>
            <div v-for="o in 100" class="text item">
              {{'消息: '+o}}
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
        notices:[]
      }
    }
  },
  components:{
    Menu,
  },
  mounted:function (){
    axios('http://localhost:8000/get_tj_datas/').then(res=>{
      this.tj_datas=res.data;
    })
  }
}
</script>

<style>
  .el-header, .el-footer {
    background: linear-gradient(to right, #a6c3fc, #f0d7fa);
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