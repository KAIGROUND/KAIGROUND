<template>
    <v-card class="ma-2">
        <!--        <v-card-title>Map</v-card-title>-->
        <div class="title grey darken-3 white--text">
            <span>Inventory</span>
        </div>
        <v-divider/>
        <v-container id="scroll-target" style="max-height: 600px; padding: 0" class="overflow-y-auto">
            <v-row no-gutters>
                <v-col cols="6" class="subtitle">
                    Attack
                </v-col>
                <v-divider vertical/>
                <v-col cols="6" class="subtitle">
                    Defense
                </v-col>
            </v-row>
            <v-divider/>
            <div v-for="i in Math.max(this.attack_item.length, this.defense_item.length)" v-bind:key="i">
                <v-row no-gutters class="ma-0" :class="i%2?'bg-grey':''">
                    <v-col cols="5" class="count" v-ripple>
                        {{(attack_item[i-1]) ? attack_item[i-1].name: ''}}
                    </v-col>
                    <v-divider vertical/>
                    <v-col cols="1" class="count">
                        {{(attack_item[i-1]) ? attack_item[i-1].count : ''}}
                    </v-col>
                    <v-divider vertical/>
                    <v-col cols="5" class="count" v-ripple>
                        {{(defense_item[i-1]) ? defense_item[i-1].name : ''}}
                    </v-col>
                    <v-divider vertical/>
                    <v-col cols="1" class="count">
                        {{(defense_item[i-1]) ? defense_item[i-1].count : ''}}
                    </v-col>
                </v-row>
                <v-divider/>
            </div>
        </v-container>

    </v-card>

</template>

<script>
    export default {
        name: "Inventory",
        data(){
            return({
                attack_item: [
                    {name: "아이템1", count:1},
                    {name: "아이템2", count:3},
                    {name: "아이템3", count:0},
                    {name: "아이템4", count:99},

                ],
                defense_item: [
                    {name: "아이템1", count:0, src:'https://img.icons8.com/ios/452/sword.png'},
                    {name: "아이템2", count:31, src: ''},
                    {name: "아이템3", count:0},
                    {name: "아이템4", count:9},
                    {name: "아이템5", count:99},
                    {name: "아이템6", count:99},
                    {name: "아이템1", count:0},
                    {name: "아이템2", count:31},
                    {name: "아이템3", count:0},
                    {name: "아이템4", count:9},
                    {name: "아이템5", count:99},
                    {name: "아이템6", count:99},
                    {name: "아이템1", count:0},
                    {name: "아이템2", count:31},
                    {name: "아이템3", count:0},
                    {name: "아이템4", count:9},
                    {name: "아이템5", count:99},
                    {name: "아이템6", count:99},
                    {name: "아이템1", count:0},
                    {name: "아이템2", count:31},
                    {name: "아이템3", count:0},
                    {name: "아이템4", count:9},
                    {name: "아이템5", count:99},
                    {name: "아이템6", count:99},
                ],
            })
        },
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
    .subtitle{
        text-align: center;
        font-size: 1em;
        font-weight: bold;
        margin: 4px -1px 4px 0;
    }
    .count{
        text-align: center;
        padding: 6px 0 6px 0;
        margin-right: -1px;
    }
    .bg-grey{
        background: #EEEEEE;
    }
</style>
