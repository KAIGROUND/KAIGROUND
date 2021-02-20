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
            <div v-for="i in Math.max(Object.keys(inventory_attack).length, Object.keys(inventory_defense).length)" v-bind:key="i">
                <v-row no-gutters class="ma-0" :class="i%2?'bg-grey':''">
                    <v-col cols="5" class="count" v-ripple style="text-align: left" @click="showDesc(Object.keys(inventory_attack)[i-1])">
                        <InventoryItem v-if="Object.keys(inventory_attack)[i-1]" :src="get_src(Object.keys(inventory_attack)[i-1])" :name="id_to_item[Object.keys(inventory_attack)[i-1]]"></InventoryItem>
                    </v-col>
                    <v-divider vertical/>
                    <v-col cols="1" class="count">
                         <div class="count-num">
                            {{(Object.keys(inventory_attack)[i-1]) ? Object.values(inventory_attack)[i-1] : ''}}
                         </div>
                    </v-col>
                    <v-divider vertical/>
                    <v-col cols="5" class="count" v-ripple style="text-align: left" @click="showDesc(Object.keys(inventory_defense)[i-1])">
                        <InventoryItem v-if="Object.keys(inventory_defense)[i-1]" :src="get_src(Object.keys(inventory_defense)[i-1])" :name="id_to_item[Object.keys(inventory_defense)[i-1]]"></InventoryItem>
                    </v-col>
                    <v-divider vertical/>
                    <v-col cols="1" class="count">
                        <div class="count-num">
                            {{(Object.keys(inventory_defense)[i-1]) ? Object.values(inventory_defense)[i-1] : ''}}
                        </div>
                    </v-col>
                </v-row>
                <v-divider/>
            </div>
        </v-container>

        <v-dialog
                v-model="dialog_a"
                max-width="460"
        >
            <InventoryDesc :id="dialog_id" :count="dialog_count"></InventoryDesc>
        </v-dialog>

    </v-card>

</template>

<script>
    import InventoryItem from "./InventoryItem";
    import InventoryDesc from "./InventoryDesc";
    export default {
        name: "Inventory",
        components: {InventoryDesc, InventoryItem},
        props: ["inventory_defense", "inventory_attack"],
        data(){
            return({
                id_to_item:['','개강','퀴즈','무거운 전공책','아침 수업','기숙사 호실이','연습반','과제','실험 수업','계절 학기','중간고사','기말고사','예습복습','낮잠','야식','튜터링','족보','공강','딸기 파티','축제','라이프','수강 철회','카이 야잠','카이 돕바','청바지','카고바지','체크남방','카이 후드티'],
                dialog_a: false,
                dialog_id: 1,
                dialog_count: 0
            })
        },
        methods:{
            get_src(id){
                try{
                    return require(`../assets/item/${id}.png`)
                } catch(e) {
                    return 'https://img.icons8.com/ios/452/sword.png'
                }
            },
            showDesc(id){
                if(id !== undefined){
                    this.dialog_a = true
                    this.dialog_id = id
                    this.dialog_count = id < 12 ? this.inventory_attack[id.toString()] : this.inventory_defense[id.toString()]
                }
            },
        },
        mounted() {
            if(this.$store.state.class === "0"){
                for(let i = 1; i <= 11; i++){
                    this.$set(this.inventory_attack, i, '')
                }
                for(let i = 12; i <= 27; i++){
                    this.$set(this.inventory_defense, i, '')
                }
            }
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
    .subtitle{
        text-align: center;
        font-size: 1em;
        font-weight: bold;
        margin: 4px -1.5px 4px 0;
    }
    .count{
        text-align: center;
        margin-right: -1.5px;
        height: 64px;
    }
    .count-num{
        padding-top: 18px;
    }
    .bg-grey{
        background: #EEEEEE;
    }
</style>
