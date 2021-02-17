<template>
    <v-card class="ma-1">
        <v-row no-gutters>
            <v-col :class="cur_turn(1)">
                <span>1st Turn</span>
            </v-col>
            <v-divider vertical/>
            <v-col :class="cur_turn(2)">
                <span>2nd Turn</span>
            </v-col>
            <v-divider vertical/>
            <v-col :class="cur_turn(3)">
                <span>3th Turn</span>
            </v-col>
            <v-divider vertical/>
            <v-col :class="cur_turn(4)">
                <span>4th Turn</span>
            </v-col>
            <v-divider vertical/>
            <v-col :class="cur_turn(5)">
                <span>5th Turn</span>
            </v-col>
            <v-divider vertical/>
            <v-col :class="cur_turn(6)">
                <span>6th Turn</span>
            </v-col>
            <v-divider vertical/>
            <v-col :class="cur_turn(7)">
                <span>7th Turn</span>
            </v-col>
            <v-divider vertical/>
            <v-col :class="cur_turn(8)">
                <span>8th Turn</span>
            </v-col>
            <v-divider vertical/>
            <v-col :class="cur_turn(9)">
                <span>9th Turn</span>
            </v-col>
            <v-divider vertical/>
            <v-col :class="cur_turn(10)">
                <span>10th Turn</span>
            </v-col>
            <v-divider vertical/>
            <v-col :class="cur_turn(11)">
                <span>11st Turn</span>
            </v-col>
            <v-divider vertical/>
            <v-col :class="cur_turn(12)">
                <span>12nd Turn</span>
            </v-col>
            <v-divider vertical/>
            <v-col :class="cur_turn(13)">
                <span>13th Turn</span>
            </v-col>
            <v-divider vertical/>
            <v-col :class="cur_turn(14)">
                <span>14th Turn</span>
            </v-col>
            <v-divider vertical/>
            <v-col :class="cur_turn(15)">
                <span>15th Turn</span>
            </v-col>
        </v-row>
    </v-card>

</template>

<script>
    export default {
        name: "Footer",
        mounted() {
            const status = this.$firebase.database().ref('status')
            status.child('turn').on("value", snapshot=>{
                this.turn = parseInt(snapshot.val())
            })
        },
        data(){
            return ({
                turn: 0
            })
        },
        methods:{
            cur_turn(idx){
                if(idx < this.turn) return "text-center rm-ma green white--text"
                else if(idx === this.turn) return "text-center rm-ma red white--text"
                else return "text-center rm-ma"
            }
        }
    }
</script>

<style scoped>
    .rm-ma{
        padding: 12px;
    }
</style>
