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
        src="/huntershow.jpg"
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
        <el-menu-item index="1" @click="returns">首页</el-menu-item>
        <el-menu-item index="2">攻略</el-menu-item>
      </el-menu>
      <div class='gameText'>
        <div
          v-for="(item, index) in gameMethod"
          :key="index"
          class="simIntroduce"
        >
          <div class="msgPhoto" @click="toDetail(item.id)">
            <img :src="item.img"/>
          </div>
          <div class="simText" @click="toDetail(item.id)">
            <div class="msgtitle">{{ item.title }}</div>
            <div class="msgDetail">{{ item.dscp }}</div>
            <div class="simTime">{{ item.date.substr(0,10)}}</div>
          </div>
        </div>

      </div>
        <div class="nav">
          <a class="arrow" @click="navChange(prev_num)"><</a>
          <div
            v-for="(item, index) in navigator"
            :key="index"
            class="navCrol"
          >
            <div v-if="item == null">
              <a class="navButton">…</a>
            </div>
            <div v-else>
              <a class="navButton" @click="navChange(navigator[index])">{{ item }}</a>
            </div>
          </div>
          <a class="arrow" @click="navChange(next_num)">></a>
        </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      activeIndex: '2',
      gameMethod: [],
      navigator: [],
      navValue: '',
      prev_num: 0,
      next_num: 0,
      navShow: true,
    }
  },
  asyncData({ params }) {
    return axios.get(`http://172.20.10.4:5000/type/0/`+ params.id).then(res => {
      return {
        gameMethod: res.data.t_list,
        navigator: res.data.pages,
        prev_num: res.data.prev_num,
        next_num: res.data.next_num
      }
    })
  },
  methods: {
    selectNav(key, keyPath) {
      console.log(key, keyPath)
    },
    toDetail(ih) {
      this.$router.push({ path:'/hunterDetail/'+ ih })
    },
    navChange(id){
      this.$router.push({ path:'/hunterWorld/'+ id })
      console.log(id,'1')
    },
    returns(){
      this.$router.push({ path:'/' })
    }
  },
  created() {

  },
}
</script>

<style lang="scss">
.background {
  .gameText {
    display: flex;
    flex-direction: column;
    background-color: #333;
    box-shadow: 0 0 5px #333;
    color: white;
    padding: 30px 0 0px 10px;
    .simIntroduce {
      display: flex;
      .simText {
        display:flex;
        flex-direction: column;
        .msgTitle {
        display: block;
        float: left;
        width: 550px;
        height: 20px;
        line-height: 20px;
        font-weight: bold;
        font-size: 18px;
        color: #dadada;
        overflow: hidden;
        white-space: nowrap;
        text-overflow: ellipsis;
        }
        .msgDetail {
          float: left;
          width: 550px;
          height: 40px;
          line-height: 20px;
          overflow: hidden;
          font-size: 12px;
          color: #bcbcbd;
          margin: 15px 0 25px;
        }
        .simTime {
          font-size: 10px;
          color: #bcbcbd;
          position: relative;
          bottom: 5px;
          left:2px;
        }
      }
      .msgPhoto {
        padding: 0 50px 20px 20px;
      }
    }
  }
  .navigator {
    box-shadow: 0 0 5px #333;
  }
  .nav{
    background-color: #333;
    color: white;
    display: flex;
    justify-content: center;
    padding-top: 30px;
    padding-bottom: 30px;
    .arrow{
      padding-right:18px;
    }
    .navCrol {
      padding-right: 15px;
      .navButton{
        padding-top:5px;
        padding: 5px 5px 5px 5px;
      }
    }
  }
}
</style>

