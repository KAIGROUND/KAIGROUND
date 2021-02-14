<template>
    <v-card class="ma-2">
<!--        <v-card-title>Map</v-card-title>-->
        <div class="title grey darken-3 white--text">
            <span>Map</span>
        </div>
        <v-divider/>
        <v-img
                max-height="600px"
                src="../assets/map.png"
        ></v-img>
    </v-card>

</template>

<script>
    export default {
        name: "Map",
        props: {},
        data(){
            return({

            })
        }
    }
</script>

<style scoped>
    .title{
        text-align: center;
        padding: 8px;
    }
    .title > span{
        font-size: 1.2em;
    }
</style>
