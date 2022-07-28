<template>
  <div id="home" style="height: 100%">
    <el-container style="height: 100%;">
      <el-aside width="200px">Aside</el-aside>
      <el-container>
        <el-header>
          <img src="" alt="">
        </el-header>
        <el-main>
          <el-card class="box-card" style="width: 30%;float: left;margin-right: 10px;">
            <div slot="header" class="clearfix">
              <span>项目总览</span>
              <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
            </div>
            <p>项目总数</p>
            <p>接口总数</p>
            <p>用例总数</p>
          </el-card>
          <el-card class="box-card" style="width: -webkit-calc(70% - 20px);float: left;">
            <div slot="header" class="clearfix">
              <span>项目总览</span>
              <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
            </div>
            <el-progress :text-inside="true" :stroke-width="13" :percentage="70"></el-progress>
            <el-progress :text-inside="true" :stroke-width="13" :percentage="100" status="success"></el-progress>
            <el-progress :text-inside="true" :stroke-width="13" :percentage="80" status="warning"></el-progress>

          </el-card>
          <el-card class="box-card" style="width: -webkit-calc(70% - 20px);float: left;">
            <div slot="header" class="clearfix">
              <span>项目总览</span>
              <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
            </div>
            <p>项目总数</p>
            <p>接口总数</p>
            <p>用例总数</p>
          </el-card>
          <el-card class="box-card" style="width: 30%;float: left;margin-left: 10px;">
            <div slot="header" class="clearfix">
              <span>项目总览</span>
              <el-button style="float: right; padding: 3px 0" type="text">操作按钮</el-button>
            </div>
            <p>项目总数</p>
            <p>接口总数</p>
            <p>用例总数</p>
          </el-card>
        </el-main>
        <el-footer style="min-height: 130px;padding-top: 15px;text-align: left;">
          <el-card class="box-card" style="width: 100%;min-height: 80%;">
            <div v-for="o in 4" :key="o" class="text item">
              {{'列表内容 ' + o }}
            </div>
          </el-card>
        </el-footer>
      </el-container>
    </el-container>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name:'home',
  components:{

  }
}
</script>

<style>
  .el-header, .el-footer {
    background-color: #B3C0D1;
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
    margin-bottom: 10px;
    overflow-y: auto;

  }
</style>