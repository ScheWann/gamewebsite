<template>
  <div class="background">
    <img
      src="/hunter.jpeg"
      :style="{
        position: 'fixed',
        zIndex: -1,
        width: '100%',
        opacity: 0.6,
      }"
    />
    <div class="allContainer">
      <img
        class="imgHeader"
        src="/hunterDetail.jpg"
        width="100%"
      />
      <el-menu
        :default-active="activeIndex"
        class="navigator"
        mode="horizontal"
        @select="selectNav"
        background-color="#232328"
        text-color="#fff"
        active-text-color="#ffd04b"
      >
        <el-menu-item index="1" @click="toList1()">首页</el-menu-item>
        <el-menu-item index="2" @click="toList2()">怪物猎人：世界</el-menu-item>
        <el-menu-item index="3" @click="toList3()">Apex英雄</el-menu-item>
        <el-menu-item index="4" @click="toList4()">只狼：影逝二度</el-menu-item>
        <el-menu-item index="5" @click="toList5()">刺客信条：奥德赛</el-menu-item>
        <el-menu-item index="6" @click="toList6()">黑暗之魂3</el-menu-item>
      </el-menu>
      <div class="article">
        <div class="articleTitle">{{ title }}</div>
        <div class="mes">
          <div class="timeWord">时间：{{ time.substr(0,10) }}</div>
          <a class="source" :href="origin" target="_blank">来源：{{ origin }}</a>
        </div>
        <div class="line"></div>
        <div class="articleContain" v-html="article"></div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      activeIndex: '2'
    }
  },
  asyncData({ params }) {
    return axios.get(`http://172.20.10.4:5000/tuto/`+ params.ih).then(res => {
      return {
        article: res.data.content,
        title: res.data.title,
        time: res.data.date,
        origin: res.data.origin
      }
    })
  },
  methods: {
    selectNav(key, keyPath) {
      console.log(key, keyPath)
    },
    toList1() {
      this.$router.push({ path:'/' })
    },
    toList2() {
      this.$router.push({ path:'/hunterWorld/2' })
    },
    toList3() {
      this.$router.push({ path:'/apex/2' })
    },
    toList4() {
      this.$router.push({ path:'/sekiro/2' })
    },
    toList5() {
      this.$router.push({ path:'/assassins/2' })
    },
    toList6() {
      this.$router.push({ path:'/darksSoul3/2' })
    }
  },
}
</script>

<style lang="scss">
.allContainer {
  background-color: white;
  .navigator {
    position: relative;
    bottom: 3px;
  }
  .article {
    padding: 50px 50px 10px 50px;
    .articleTitle {
      text-align: center;
      padding-bottom: 50px;
      font-size: 20px;
      font-weight: bold;
    }
    .mes {
      display: flex;
      .timeWord {
        font-size: 13px;
        color: #959595;
        line-height: 40px;
      }
      .source {
        font-size: 13px;
        color: #959595;
        line-height: 40px;
        padding-left: 50px;
      }
    }
    .line {
      border-bottom: 1px solid #959595;
    }
    .articleContain {
      padding-top: 20px;
      padding-bottom: 100px;
      p {
        text-indent: 2em;
        font-size: 15px;
        line-height: 30px;
        color: #333;
        margin: 10px auto;
        img{
          width: 800px;
          padding-right: 25px;
        }
      }
    }
  }
}
</style>


