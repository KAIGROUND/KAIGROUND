<template>
    <v-card class="ma-1">
        <v-row no-gutters>
            <v-col class="title grey darken-3 white--text">
                Turn
            </v-col>
            <v-divider vertical/>
            <v-col class="span-data">
                <div>Move</div>
                <v-divider/>
                <div>00:00</div>
            </v-col>
            <v-divider vertical/>
            <v-col class="span-data red white--text">
                <div>Battle</div>
                <v-divider/>
                <div>00:00</div>
            </v-col>
            <v-divider vertical/>
            <v-col class="span-data">
                <div>Game</div>
                <v-divider/>
                <div>00:00</div>
            </v-col>
        </v-row>
    </v-card>
</template>

<script>
    export default {
        name: "Turn"
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
    }

</style>
