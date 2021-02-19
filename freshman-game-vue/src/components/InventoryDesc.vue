<template>
    <v-card
            class="mx-auto"
            :max-width="narrow ? 230 : 460"
    >

        <v-img
                :height="narrow ? 160 : 250"
                :src="get_src(this.id)"
        ></v-img>

        <v-card-title>{{id_to_item[id]}}</v-card-title>

        <v-card-text>
            <v-row
                    align="center"
                    class="mx-0"
            >
                <v-rating
                        :value="val1"
                        color="amber"
                        dense
                        half-increments
                        readonly
                        size="14"
                        v-if="!narrow"
                ></v-rating>

                <div class="grey--text ml-4 mr-4" v-if="!narrow">
                    {{att}}
                </div>

                <v-rating
                        :value="val2"
                        color="amber"
                        dense
                        half-increments
                        readonly
                        size="14"
                        v-if="this.id <= 11 && !narrow"
                ></v-rating>

                <div class="grey--text ml-4 mr-4" v-if="this.id <= 11 && !narrow">
                    {{att2}}
                </div>
            </v-row>

            <div class="grey--text mr-4 fs mt-4" v-if="narrow">
                {{att}}
            </div>
            <div class="grey--text mr-4 fs" v-if="this.id <= 11 && narrow">
                {{att2}}
            </div>

            <div class="my-4 subtitle-1">
                {{count ? count + '개 보유중' : ''}}
            </div>

            <div>{{item_desc[this.id]}}</div>
        </v-card-text>

    </v-card>
</template>

<script>
    export default {
        name: "InventoryDesc",
        props: ['id', 'count', 'narrow'],
        data(){
            return({
                id_to_item:['','개강','퀴즈','무거운 전공책','아침 수업','기숙사 호실이동','연습반','과제','실험 수업','계절 학기','중간고사','기말고사','예습복습','낮잠','야식','튜터링','족보','공강','딸기 파티','축제','라이프','수강 철회','카이 야잠','카이 돕바','청바지','카고바지','체크남방','카이 후드티'],
                id_to_desc:[],
                id1_to_att:[0,1,2,2,2,4,4,4,4,4,6,8],
                id1_to_range:[0,10,6,2,4,1,2,3,3,3,2,4],
                id12_to_def:[1,1,1,1,3,3,3,3,5,7,0,0,0,0,0,0],
                id12_to_hlt:[0,0,0,0,0,0,0,0,0,0,2,2,1,1,2,2],
                item_desc:[],
                title: this.id
            })
        },
        created() {
            for(let i=0;i<28;i++){
                this.item_desc.push(i + "경우, 특히 AngularJS를 사용하던 경우 watch를 남용하는 경우가 있습니다. 하지만 명령적인 watch 콜백보다 computed 속성을 사용하는 것이 더 좋습니다.")
            }
        },
        methods:{
            get_src(id){
                try{
                    return require(`../assets/ItemImage/${id}.png`)
                } catch(e) {
                    return 'https://img.icons8.com/ios/452/sword.png'
                }
            },
        },
        computed:{
            att(){
                return (this.id <= 11) ? '공격력: ' + this.id1_to_att[this.id] : (this.id <= 21) ? '방어력: ' + this.id12_to_def[this.id-12] : '리스폰시 추가 체력: ' + this.id12_to_hlt[this.id-12]
            },
            att2(){
                return (this.id <= 11) ? '공격 가능 범위: ' + this.id1_to_range[this.id] : ''
            },
            val1(){
                return (this.id <= 11) ? this.id1_to_att[this.id]/2 : (this.id <= 21) ? this.id12_to_def[this.id-12]/2 : this.id12_to_hlt[this.id-12]
            },
            val2(){
                return (this.id <= 11) ? this.id1_to_range[this.id]/2 : ''
            }
        }
    }
</script>

<style scoped>
    .fs{
        font-size: 1.3em;
        line-height: 1.6;
    }
</style>
