<template>
  <v-app>
    <div class="wrapper">

      <v-container class="grey lighten-5">
        <Minigame v-if="minigame_mode" :prices="prices" :mode="mode" @minidone="mini_done"/>
        <v-row no-gutters dense v-if="!minigame_mode">
          <v-col cols="5">
            <Map :accent="map_accent_num"/>
          </v-col>
          <v-col cols="2">
            <Stamina @class_accent="map_class_accent" @class_restore="map_class_restore"/>
          </v-col>
          <v-col cols="2">
            <Point/>
          </v-col>
          <v-col cols="3">
            <Inventory :inventory_attack="inventory_attack" :inventory_defense="inventory_defense"/>
          </v-col>
        </v-row>
        <v-row no-gutters dense>
          <v-col v-if="$store.state.class !== '0'" cols="5">
            <Status :mode="mode" :turn="turn" :inventory_attack="inventory_attack" :inventory_defense="inventory_defense" :team_list="team_list" @ainv="update_ainv" @dinv="update_dinv"/>
          </v-col>
          <v-col :cols="$store.state.class !== '0' ? '3' : '8'">
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
          <v-col cols="3" >
            <v-icon @click="launch_minigame" v-if="$store.state.class !== '0'">mdi-controller-classic</v-icon>
          </v-col>
          <v-col cols="6">
            <v-card v-if="turn >= 8" class="mt-2 pa-4">
              <div>[특별상] 다리 아프겠다...: 시작부터 게임이 끝날 때까지 이동한 거리가 가장 긴 팀이 수상!</div>
              <div>[특별상] 21학번 환영해요: 21등 팀에게 수상!</div>
            </v-card>
          </v-col>
          <v-col cols="3">
            <Header/>
          </v-col>
        </v-row>
      </v-container>
    </div>
    <Result v-if="show_result" @close="show_result = false" :result_data="result_data"></Result>
    <v-dialog
            v-model="dialog_8"
            persistent
            max-width="1000"
    >
      <v-card>
        <div class="game-progressing">특별상 2개가 공개 됩니다!</div>
        <div class="game-progressing-sub">1. 다리 아프겠다...: 시작부터 게임이 끝날 때까지 이동한 거리가 가장 긴 팀이 수상!</div>
        <div class="game-progressing-sub">2. 21학번 환영해요: 21등 팀에게 수상!</div>
      </v-card>
    </v-dialog>
    <Timer :show="timer_dialog" @show_cd="show_cd"></Timer>
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
import Result from "./Result";
import Timer from "./Timer";

export default {
  name: 'App',

  components: {
    Timer,
    Result,
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
      mode: 3,
      timer: 0,
      turn: 0,
      map_accent_num: 0,
      inventory_attack: {},
      inventory_defense: {},
      armor_top: 0,
      armor_bottom: 0,
      team_list: {},
      prices: {},
      show_result: false,
      result_data: null,
      minigame_mode: false,
      dialog_8: false,
      timer_dialog: false,
    })
  },

  mounted() {
    const db = this.$firebase.database()
    const status = db.ref('status')
    status.child('mode').on("value", snapshot=>{
      this.mode = snapshot.val()
      this.minigame_mode = false
      this.timer_dialog = snapshot.val() === 4;
      if(snapshot.val() !== 3){
        this.get_time_idx(val => {
          const time_conf = db.ref('time_conf')
          time_conf.once("value", snapshot => {
            let T = snapshot.val()
            this.run_timer(val, T)
          })
          if(this.$store.state.class !== "0") this.onChangeMode()
        });
      }
    })

    status.child('turn').on("value", snapshot=>{
      this.turn = parseInt(snapshot.val())
      if(snapshot.val() === 8){
        this.dialog_8 = true
        setTimeout(() => {
          this.dialog_8 = false
        }, 5000)
      }
    })

    db.ref('winner').on("value", snapshot=>{
      const final_result = snapshot.val()
      if(final_result){
        this.result_data = final_result[this.$store.state.class] ?? null;
        if(this.result_data) this.show_result = true
      }
    })
  },

  methods: {
    get_time_idx(func){
      const status = this.$firebase.database().ref('status')
      status.child('time_idx').once("value", snapshot => {
        func(snapshot.val());
      })
    },

    run_timer(val, T) {
      let timer = 0
      if(this.mode === 0){
        timer = T[0] - val % (T[0] + T[1] + T[2] + T[3] + T[4] + T[5])
      } else if(this.mode === 1){
        timer = T[2] - (val - (T[0] + T[1])) % (T[0] + T[1] + T[2] + T[3] + T[4] + T[5])
      } else if(this.mode === 2){
        timer = T[4] - (val - (T[0] + T[1] + T[2] + T[3])) % (T[0] + T[1] + T[2] + T[3] + T[4] + T[5])
      }

      if(timer < 0){
        setTimeout(() => {
          this.get_time_idx(new_val => {
            this.run_timer(new_val, T)
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
          if (this.timer <= 0 || this.mode === 3) {
            clearInterval(looper)
            this.mode = 3
          }
        }, 1000)
      } else {
        this.timer = 0
        this.mode = 3
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
        this.team_list= JSON.parse(result.data.team_list)
      })

    },

    launch_minigame(){
      if(!this.minigame_mode && this.mode === 1){
        this.$http.get(`${this.$host}minigame?me=${this.$store.state.class}`).then(result =>{
            this.prices = JSON.parse(result.data.data)
            this.minigame_mode = true
        })
      } else this.minigame_mode = false
    },
    update_ainv(list){
      this.inventory_attack=list
      this.launch_minigame()
    },
    update_dinv(list){
      this.inventory_defense=list
    },
    mini_done(){
      this.minigame_mode = false
    },
    map_class_accent(idx){
      this.map_accent_num=idx
    },
    map_class_restore(){
      this.map_accent_num=0
    },
    show_cd(b){
      this.timer_dialog = b
    }
  }
};
</script>

<style scoped>
  .container{
    max-width: 1650px;
  }

  .game-progressing{
    font-size: 2em;
    text-align: center;
    padding: 24px;
    font-weight: bold;
  }

  .game-progressing-sub{
    font-size: 1.3em;
    text-align: center;
    padding: 8px;
  }
</style>
