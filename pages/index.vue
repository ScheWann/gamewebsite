<template>
  <div class="body">
    <div class="transition">
      <img
        src="/hunter.jpeg"
        :style="{
          position: 'fixed',
          zIndex: -1,
          width: '100%',
          opacity: img1
        }"
      />
      <img
        src="/apex.jpg"
        :style="{
          position: 'fixed',
          zIndex: -1,
          width: '100%',
          opacity: img2
        }"
      />
      <img
        src="/wolf.jpeg"
        :style="{
          position: 'fixed',
          zIndex: -1,
          width: '100%',
          opacity: img3
        }"
      />
      <img
        src="/assassins.jpeg"
        :style="{
          position: 'fixed',
          zIndex: -1,
          width: '100%',
          opacity: img4
        }"
      />
      <img
        src="/darksoul.jpg"
        :style="{
          position: 'fixed',
          zIndex: -1,
          width: '100%',
          opacity: img5
        }"
      />
    </div>
    <div class="container">
      <div class="header">
        <h1>Pytutorial</h1>
        <div class="navigater">
          <h5 @click="game1(page)">Monster Hunter:World</h5>
          <h5 @click="game2(page)">Apex</h5>
          <h5 @click="game3(page)">Sekiro: Shadows Die Twice</h5>
          <h5 @click="game4(page)">Assassin's Creed Odyssey</h5>
          <h5 @click="game5(page)">Dark Souls Ⅲ</h5>
        </div>
      </div>
      <div class="content" style="background-color: white;opacity: 0.6">
        <input class="inputBox" v-model="inputWord" @keyup.enter="searchEnterFun(inputWord)" placeholder="Sreach On"/>
      </div>
    </div>
  </div>
</template>

<script>
import { async } from 'q';
export default {
  data() {
    return {
      img1: 1,
      img2: 0,
      img3: 0,
      img4: 0,
      img5: 0,
      flag: 1,
      page: 2,
      inputWord:''
    }
  },
  methods: {
    game1(id) {
      this.$router.push({ path:'/hunterWorld/'+ id })
    },
    game2(id) {
      this.$router.push({ path:'/apex/'+ id })
    },
    game3(id) {
      this.$router.push({ path:'/sekiro/'+ id })
    },
    game4(id) {
      this.$router.push({ path:'/assassins/'+ id })
    },
    game5(id) {
      this.$router.push({ path:'/darksSoul3/'+ id })
    },
    searchEnterFun(iWord) {
      this.$router.push({ path:'/search/'+ iWord })
    }
  },
  created() {
    setInterval(() => {
      if (this.flag === 1) {
        const timer = setInterval(() => {
          this.img1 = this.img1 - 0.005
          this.img2 = this.img2 + 0.005
        }, 1)
        setTimeout(() => {
          clearInterval(timer)
          this.img1 = 0
          this.img2 = 1
          this.flag = 2
        }, 999)
      }
      if (this.flag === 2) {
        const timer = setInterval(() => {
          this.img2 = this.img2 - 0.005
          this.img3 = this.img3 + 0.005
        }, 1)
        setTimeout(() => {
          clearInterval(timer)
          this.img2 = 0
          this.img3 = 1
          this.flag = 3
        }, 999)
      }
      if (this.flag === 3) {
        const timer = setInterval(() => {
          this.img3 = this.img3 - 0.005
          this.img4 = this.img4 + 0.005
        }, 1)
        setTimeout(() => {
          clearInterval(timer)
          this.img3 = 0
          this.img4 = 1
          this.flag = 4
        }, 999)
      }
      if (this.flag === 4) {
        const timer = setInterval(() => {
          this.img4 = this.img4 - 0.005
          this.img5 = this.img5 + 0.005
        }, 1)
        setTimeout(() => {
          clearInterval(timer)
          this.img4 = 0
          this.img5 = 1
          this.flag = 5
        }, 999)
      }
      if (this.flag === 5) {
        const timer = setInterval(() => {
          this.img5 = this.img5 - 0.005
          this.img1 = this.img1 + 0.005
        }, 1)
        setTimeout(() => {
          clearInterval(timer)
          this.img5 = 0
          this.img1 = 1
          this.flag = 1
        }, 999)
      }
    }, 4003)
  }
}
</script>
<style lang="scss">
.inputBox {
  width: 100%;
  outline-color: invert ;
	outline-style: none ;
	outline-width: 0px ;
	border: none ;
	border-style: none ;
	text-shadow: none ;
	-webkit-appearance: none ;
	-webkit-user-select: text ;
	outline-color: transparent ;
  box-shadow: none;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align:center;
  font-size: 3rem;
}
.header {
  display: flex;
  justify-content: space-between;
	position: absolute;
	top: 20%;
	left: 54%;
	margin-top: -90px;
	margin-left: -500px;
  cursor: default;
  .navigater {
    display: flex;
    align-items: center;
    padding-left: 185px;
  }
  h1 {
    color: white;
    text-shadow:0 0 10px #000;
    padding-right:30px;
    padding-bottom: 20px;
  }
  h5 {
    color: white;
    text-shadow:0 0 10px #000;
    padding-right:30px;
    padding-bottom: 20px;
  }
}
</style>
