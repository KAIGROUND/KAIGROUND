<template>
  <v-app>
    <div class="wrapper">

      <v-container class="grey lighten-5">
        <Minigame v-if="minigame_mode" :prices="prices" @minidone="mini_done"/>
        <v-row no-gutters dense v-if="!minigame_mode">
          <v-col cols="5">
            <Map/>
          </v-col>
          <v-col cols="2">
            <Stamina/>
          </v-col>
          <v-col cols="2">
            <Point/>
          </v-col>
          <v-col cols="3">
            <Inventory :inventory_attack="inventory_attack" :inventory_defense="inventory_defense"/>
          </v-col>
        </v-row>
        <v-row no-gutters dense>
          <v-col cols="5">
            <Status :mode="mode" :turn="turn" :inventory_attack="inventory_attack" :inventory_defense="inventory_defense" :team_list="team_list" @ainv="update_ainv" @dinv="update_dinv"/>
          </v-col>
          <v-col cols="3">
            <Turn :timer="timer" :mode="mode"/>
          </v-col>
          <v-col cols="4">
            <Armor :top="armor_top" :bottom="armor_bottom"/>
          </v-col>
        </v-row>
        <v-row no-gutters>
          <v-col cols="12">
            <Footer :turn="turn"/>
          </v-col>
        </v-row>
        <v-row no-gutters dense>
          <v-col cols="1" >
            <v-icon @click="launch_minigame">mdi-controller-classic</v-icon>
          </v-col>
          <v-col cols="11">
            <Header/>
          </v-col>
        </v-row>
      </v-container>
    </div>
  </v-app>
</template>

<script>
import Map from './Map'
import Stamina from "@/components/Stamina";
import Point from "@/components/Point";
import Inventory from "@/components/Inventory";
import Status from "@/components/Status";
import Turn from "@/components/Turn";
import Armor from "@/components/Armor";
import Footer from "@/components/Footer";
import Header from "./Header";
import Minigame from "./Minigame";

export default {
  name: 'App',

  components: {
    Minigame,
    Footer,
    Armor,
    Turn,
    Status,
    Inventory,
    Map,
    Stamina,
    Point,
    Header
  },

  data(){
    return ({
      time_idx: 0,
      mode: 2,
      timer: 0,
      turn: 0,
      inventory_attack: {},
      inventory_defense: {},
      armor_top: 0,
      armor_bottom: 0,
      team_list: {},
      prices: {},
      minigame_mode: false,
    })
  },

  mounted() {
    const status = this.$firebase.database().ref('status')
    status.child('mode').on("value", snapshot=>{
      this.mode = snapshot.val()
      if(snapshot.val() !== 2){
        this.get_time_idx(val => {
          this.run_timer(val)
          this.onChangeMode()
        });
      } else {
        this.minigame_mode = false;
      }
    })

    status.child('turn').on("value", snapshot=>{
      this.turn = parseInt(snapshot.val())
    })
  },

  methods: {
    get_time_idx(func){
      const status = this.$firebase.database().ref('status')
      status.child('time_idx').once("value", snapshot => {
        func(snapshot.val());
      })
    },

    run_timer(val) {
      const T=[120,5,300,5]
      let timer = 0
      if(this.mode === 0){
        timer = T[0] - val % (T[0] + T[1] + T[2] + T[3])
      } else if(this.mode === 1){
        timer = T[2] - (val - (T[0] + T[1])) % (T[0] + T[1] + T[2] + T[3])
      }

      if(timer < 0){
        setTimeout(() => {
          this.get_time_idx(new_val => {
            this.run_timer(new_val)
          });
        }, 1000)
        return;
      } else {
        this.timer = timer;
        this.time_idx = val
      }

      if(this.timer > 3) { // 버그 방지
        let looper = setInterval(() => {
          this.timer--
          if (this.timer <= 0 || this.mode === 2) {

            clearInterval(looper)
            this.mode = 2
          }
        }, 1000)
      } else {
        this.timer = 0
        this.mode = 2
      }
    },

    onChangeMode(){
      this.$http.get(`${this.$host}inventory?me=${this.$store.state.class}`).then(result => {
        this.inventory_attack = JSON.parse(result.data.attack_list)
        this.inventory_defense = JSON.parse(result.data.defense_list)
        this.armor_top = result.data.top
        this.armor_bottom = result.data.bottom
      })
      this.$http.get(`${this.$host}get_attack?me=${this.$store.state.class}`).then(result => {
        console.log(result.data.team_list)
        this.team_list= JSON.parse(result.data.team_list)
      })

    },

    launch_minigame(){
      if(!this.minigame_mode){
        this.$http.get(`${this.$host}minigame?me=${this.$store.state.class}`).then(result =>{
          this.prices = JSON.parse(result.data.data)
          this.minigame_mode = true
        })
      } else this.minigame_mode = false
    },
    update_ainv(list){
      this.inventory_attack=list
    },
    update_dinv(list){
      this.inventory_defense=list
    },
    mini_done(){
      this.minigame_mode = false
    }
  }
};
</script>

<style scoped>
  .container{
    max-width: 1650px;
  }
</style>
