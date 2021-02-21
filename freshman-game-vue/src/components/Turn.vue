<template>
    <v-card class="ma-1">
        <v-row no-gutters>
            <v-col class="title grey darken-3 white--text" cols="3">
                Turn
            </v-col>
            <v-col :class="this.mode === 0?'span-data red white--text':'span-data'" cols="3">
                <div>Move</div>
                <v-divider/>
                <div style="font-size: 1.4em; line-height: 1.0;">{{counter(0)}}</div>
            </v-col>
            <v-divider vertical style="margin-left: -1px"/>
            <v-col :class="this.mode === 1?'span-data red white--text':'span-data'" cols="3">
                <div :style="$store.state.class === '0' ? '' : 'margin: -13px 0'">Attack / Game</div>
                <v-divider/>
                <div style="font-size: 1.4em; line-height: 1.0;">{{counter(1)}}</div>
            </v-col>
            <v-divider vertical style="margin-left: -1px"/>
            <v-col :class="this.mode === 2?'span-data red white--text':'span-data'" cols="3">
                <div style="margin: 0 -2px">Defense</div>
                <v-divider/>
                <div style="font-size: 1.4em; line-height: 1.0;">{{counter(2)}}</div>
            </v-col>
        </v-row>
    </v-card>
</template>

<script>

    export default {
        name: "Turn",
        props: ['mode', 'timer'],
        methods: {
            counter(mode){
                if(this.mode === mode){
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
