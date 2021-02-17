<template>
    <v-card class="ma-1">
        <v-row no-gutters>
            <v-col class="title grey darken-3 white--text" cols="3">
                Turn
            </v-col>
            <v-col :class="this.mode === 0?'span-data red white--text':'span-data'" cols="3">
                <div>Move</div>
                <v-divider/>
                <div>{{mv}}</div>
            </v-col>
            <v-divider vertical/>
            <v-col :class="this.mode === 1?'span-data red white--text':'span-data'" cols="6">
                <div>Battle / Game</div>
                <v-divider/>
                <div>{{bg}}</div>
            </v-col>
        </v-row>
    </v-card>
</template>

<script>

    export default {
        name: "Turn",
        data(){
            return ({
                mode: 2,
                time_idx: 0,
                timer: 0,
            })
        },
        mounted() {
            const status = this.$firebase.database().ref('status')
            status.child('mode').on("value", snapshot=>{
                this.mode = snapshot.val()
                if(snapshot.val() !== 2){
                    this.get_time_idx(val => {
                        this.time_idx = val
                        this.run_timer()
                    });
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
            run_timer(){
                const T=[120,5,300,5]
                if(this.mode === 0){
                    this.timer = T[0] - this.time_idx % (T[0] + T[1] + T[2] + T[3])
                } else if(this.mode === 1){
                    this.timer = T[2] - (this.time_idx - (T[0] + T[1])) % (T[0] + T[1] + T[2] + T[3])
                }

                if(this.timer > 3) { // 버그 방지
                    let looper = setInterval(() => {
                        this.timer--
                        if (this.timer <= 0) {
                            clearInterval(looper)
                            this.mode = 2
                        }
                    }, 1000)
                } else {
                    this.timer = 0
                    this.mode = 2
                }
            }
        },
        computed: {
            mv(){
                if(this.mode === 0){
                    const min = Math.floor(this.timer / 60)
                    const sec = this.timer % 60
                    return `${min}:${sec > 9 ? sec : '0' + sec}`
                } else return '0:00'
            },
            bg(){
                if(this.mode === 1){
                    const min = Math.floor(this.timer / 60)
                    const sec = this.timer % 60
                    return `${min}:${sec > 9 ? sec : '0' + sec}`
                } else return '0:00'
            }
        }

    }
</script>

<style scoped>
    .span-data{
        font-size: 1.1em;
        text-align: center;
    }

    .span-data > div{
        padding: 18px;
    }

    .title{
        text-align: center;
        line-height: 125px;
        font-size: 1.2em;
        margin-right: -1px;
    }

</style>
