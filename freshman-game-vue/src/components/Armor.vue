<template>
    <v-card class="ma-1">
        <v-row no-gutters>
            <v-col class="title grey darken-3 white--text">
                Armor
            </v-col>
            <v-divider vertical/>
            <v-col class="sub-text sub-head sub-small" cols="2">
                top
            </v-col>
            <v-col class="sub-text" cols="3">
                asdfas
            </v-col>
            <v-col class="sub-text sub-head sub-small" cols="2">
                bottom
            </v-col>
            <v-col class="sub-text" cols="3">
                asdfas
            </v-col>
        </v-row>
    </v-card>
</template>

<script>
    export default {
        name: "Armor"
    }
</script>

<style scoped>
    .sub-text{
        line-height: 125px;
        text-align: center;
    }

    .sub-head{
        background: #DDDDDD;
        font-size: 1em;
    }

    .title{
        text-align: center;
        line-height: 125px;
        font-size: 1.2em;
    }
</style>
