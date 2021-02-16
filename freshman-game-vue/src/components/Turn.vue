<template>
    <v-card class="ma-1">
        <v-row no-gutters>
            <v-col class="title grey darken-3 white--text" cols="3">
                Turn
            </v-col>
            <v-divider vertical/>
            <v-col class="span-data" cols="3">
                <div>Move</div>
                <v-divider/>
                <div v-if="this.time !== -1">{{time}}</div>
            </v-col>
            <v-divider vertical/>
            <v-col class="span-data red white--text" cols="6">
                <div>Battle / Game</div>
                <v-divider/>
                <div>00:00</div>
            </v-col>
        </v-row>
    </v-card>
</template>

<script>
    export default {
        name: "Turn",
        data(){
            return ({
                mode: -1,
                time: -1,
            })
        },
        mounted(){

            this.$socket.on('LEFT_TIME', data => {
                console.log(data)
                this.time = data
            })

            this.$socket.emit('req_time', {message: '200'})
        },

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
        margin-left: -2px;;
    }

</style>
