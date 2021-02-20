<template>
    <v-card class="ma-1">
        <v-row no-gutters>
            <v-col class="title grey darken-3 white--text" cols="3">
                Turn
            </v-col>
            <v-col :class="this.mode === 0?'span-data red white--text':'span-data'" cols="3">
                <div>Move</div>
                <v-divider/>
                <div style="font-size: 1.4em; line-height: 1.0;">{{mv}}</div>
            </v-col>
            <v-divider vertical/>
            <v-col :class="this.mode === 1?'span-data red white--text':'span-data'" cols="6">
                <div>Battle / Game</div>
                <v-divider/>
                <div style="font-size: 1.4em; line-height: 1.0;">{{bg}}</div>
            </v-col>
        </v-row>
    </v-card>
</template>

<script>

    export default {
        name: "Turn",
        props: ['mode', 'timer'],
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
        margin-right: -2px;
    }

</style>
