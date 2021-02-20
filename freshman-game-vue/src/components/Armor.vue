<template>
    <v-card class="ma-1">
        <v-row no-gutters>
            <v-col class="title grey darken-3 white--text">
                Armor
            </v-col>
            <v-divider vertical/>
            <v-col class="sub-text sub-head sub-small" cols="2">
                Top
            </v-col>
            <v-col cols="3" @click="showDesc(top)">
                <div class="im-text" >
                    <v-img style="margin-left: 20px" :src="get_src(top)" width="100px" height="100px">
                    </v-img>
                    <span>{{get_text(top)}}</span>
                </div>
            </v-col>
            <v-col class="sub-text sub-head sub-small" cols="2">
                Bottom
            </v-col>
            <v-col class="" cols="3" @click="showDesc(bottom)">
                <div class="im-text">
                    <v-img style="margin-left: 20px" :src="get_src(bottom)" width="100px" height="100px"/>
                    <span>{{get_text(bottom)}}</span>
                </div>
            </v-col>
        </v-row>

        <v-dialog
                v-model="dialog_a"
                max-width="460"
        >
            <InventoryDesc :id="dialog_id"></InventoryDesc>
        </v-dialog>

    </v-card>
</template>

<script>
    import InventoryDesc from "./InventoryDesc";
    export default {
        name: "Armor",
        components: {InventoryDesc},
        props: ['top', 'bottom'],
        data(){
            return({
                armor_name: ['카이 야잠','카이 돕바','청바지','카고바지','체크남방','카이 후드티'],
                dialog_a:false,
                dialog_id:0,
            })
        },
        methods:{
            get_src(id){
                try{
                    return require(`../assets/item/${id}.png`)
                } catch(e) {
                    return ''
                }
            },
            get_text(id){
                return this.armor_name[id-22]??''
            },
            showDesc(id){
                if(id !== undefined && id >= 22){
                    this.dialog_a = true
                    this.dialog_id = id
                }
            }
        },
    }
</script>

<style scoped>
    .sub-text{
        text-align: center;
        line-height: 125px;
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

    .im-text{
        vertical-align: center;
        text-align: center;
    }
</style>
