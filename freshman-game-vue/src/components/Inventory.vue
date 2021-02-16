<template>
    <v-card class="ma-2">
        <!--        <v-card-title>Map</v-card-title>-->
        <div class="title grey darken-3 white--text">
            <span>Inventory</span>
        </div>
        <v-divider/>
        <v-container id="scroll-target" style="max-height: 620px; padding: 0" class="overflow-y-auto">
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
                        <InventoryItem v-if="attack_item[i-1]" :src="attack_item[i-1].src" :name="attack_item[i-1].name"></InventoryItem>
                    </v-col>
                    <v-divider vertical/>
                    <v-col cols="1" class="count">
                         <span>
                            {{(attack_item[i-1]) ? attack_item[i-1].count : ''}}
                         </span>
                    </v-col>
                    <v-divider vertical/>
                    <v-col cols="5" class="count" v-ripple>
                        <InventoryItem v-if="defense_item[i-1]" :src="defense_item[i-1].src" :name="defense_item[i-1].name"></InventoryItem>
                    </v-col>
                    <v-divider vertical/>
                    <v-col cols="1" class="count">
                        <span>
                            {{(defense_item[i-1]) ? defense_item[i-1].count : ''}}
                        </span>
                    </v-col>
                </v-row>
                <v-divider/>
            </div>
        </v-container>

    </v-card>

</template>

<script>
    import InventoryItem from "./InventoryItem";
    export default {
        name: "Inventory",
        components: {InventoryItem},
        data(){
            return({
                attack_item: [
                    {name: "아이템1", count:1, src:'../assets/test1.png'},
                    {name: "아이2", count:3, src:'https://i.pinimg.com/originals/f8/4a/7d/f84a7d952cc7ac55b025f2ea28cbc2cc.jpg'},
                    {name: "템3", count:0, src:'https://img.icons8.com/ios/452/sword.png'},
                    {name: "아이템4", count:99, src:'https://img.icons8.com/ios/452/sword.png'},

                ],
                defense_item: [
                    {name: "아이템1", count:0, src:'https://img.icons8.com/ios/452/sword.png'},
                    {name: "아이템2", count:31, src:'https://img.icons8.com/ios/452/sword.png'},
                    {name: "아이템아이템", count:0, src:'https://i.pinimg.com/originals/f8/4a/7d/f84a7d952cc7ac55b025f2ea28cbc2cc.jpg'},
                    {name: "아이템1", count:0, src:'https://img.icons8.com/ios/452/sword.png'},
                    {name: "아이템2", count:31, src:'https://img.icons8.com/ios/452/sword.png'},
                    {name: "아이템아이템", count:0, src:'https://i.pinimg.com/originals/f8/4a/7d/f84a7d952cc7ac55b025f2ea28cbc2cc.jpg'},
                    {name: "아이템1", count:0, src:'https://img.icons8.com/ios/452/sword.png'},
                    {name: "아이템2", count:31, src:'https://img.icons8.com/ios/452/sword.png'},
                    {name: "아이템아이템3", count:0, src:'https://i.pinimg.com/originals/f8/4a/7d/f84a7d952cc7ac55b025f2ea28cbc2cc.jpg'},
                    {name: "아이템1", count:0, src:'https://img.icons8.com/ios/452/sword.png'},
                    {name: "아이템2", count:31, src:'https://img.icons8.com/ios/452/sword.png'},
                    {name: "아이템아이3", count:0, src:'https://i.pinimg.com/originals/f8/4a/7d/f84a7d952cc7ac55b025f2ea28cbc2cc.jpg'},
                    {name: "아이템1", count:0, src:'https://img.icons8.com/ios/452/sword.png'},
                    {name: "아이템2", count:31, src:'https://img.icons8.com/ios/452/sword.png'},
                    {name: "아아이3", count:0, src:'https://i.pinimg.com/originals/f8/4a/7d/f84a7d952cc7ac55b025f2ea28cbc2cc.jpg'},
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
        margin-right: -1.5px;
        height: 48px;
    }
    .count > span{
        line-height: 2.8;
    }
    .bg-grey{
        background: #EEEEEE;
    }
</style>
