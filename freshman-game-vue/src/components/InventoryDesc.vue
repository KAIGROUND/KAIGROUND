<template>
    <v-card
            class="mx-auto"
            :max-width="narrow ? 230 : 460"
            :height="narrow ? 400 : 'auto'"
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
                        :value="val1/2"
                        color="amber"
                        dense
                        half-increments
                        readonly
                        size="14"
                        v-if="!narrow"
                ></v-rating>

                <div class="black--text ml-4 mr-4" v-if="!narrow">
                    {{att}}
                </div>

                <v-rating
                        :value="val2*2"
                        color="amber"
                        dense
                        half-increments
                        readonly
                        size="14"
                        v-if="this.id <= 11 && !narrow"
                ></v-rating>

                <div class="black--text ml-4 mr-4" v-if="this.id <= 11 && !narrow">
                    {{att2}}
                </div>
            </v-row>

            <div class="black--text mr-4 fs mt-4" v-if="narrow">
                {{att}}
            </div>
            <div class="black--text mr-4 fs" v-if="this.id <= 11 && narrow">
                {{att2}}
            </div>

            <div class="my-4 subtitle-1">
                {{count ? count + '개 보유중' : ''}}
            </div>

            <div class="black--text">
                {{item_desc[this.id]}}
            </div>
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
                item_desc:[" ", "개강, 수많은 학부생이 개강 전날 술을 마시곤 한다.", "주로 금요일에 있다. 퀴즈를 잘 보면 그날은 기분이 좋더라.", "진짜 엄청 무겁다. 태블릿 사는 것을 추천", "안 듣는 것이 낫다, 후회할 가능성이 높다.", "짐을 들고 오르내리다 보면 전완근이 아려 오기 시작한다.", "조교님이 진행하시는 연습반. 수업에 모르는 부분이 있었다면 연습반 시간에 물어보자.", "귀찮긴 하지만 이거 없으면 학기 중에 공부 1도 안하니까 열심히 하자.", "원래대로라면 직접 실험을 했겠지만 비대면으로 인해 보고서만 작성하고 제출하면 된다.", "성실한 학생이라면 방학에도 계절학기를 들어 학점을 채울 수 있다.", "새내기가 치르는 첫 대학 시험. 모두 화이팅!", "머리가 아플 수도 있지만 방학 생각 하나로 버틴다.", "매 학기 초 예습, 복습 계획을 세우지만 번번히 실패하곤 한다.", "점심 먹고 강의를 듣다 보면 스르륵 감기는 눈꺼풀...", "이건 못 참지!", "공짜로 받을 수 있는 기초과목 과외. 부담되는 과목이 있다면 신청하도록 하자.", "족발보쌈....이 아니라 대대로 내려온 시험지 등. 알차게 활용하고 물려주도록 하자.", "갑자기 생긴 공강만큼 기분 좋은 게 없다.", "잔디밭에 돗자리를 펴 놓고 오순도순 딸기를 먹는 파티.... 였던 것.", "나도 궁금하다(지나가던 20학번)", "자다가 수업을 결석한 날이면 이 과목에 라이프가 있었기를 기도하곤 한다.", "빠드익선", "이걸 입으면 진짜 대학생이 된 기분이 든다.", "단돈 5만원으로 겨울을 따뜻하게 보낼 수 있다.", "무난한 청바지", "평범한 카고바지. 주머니가 많지만 실제로 물건을 넣지는 않는다.", "공대생이라면 체크남방 하나쯤은 있어야지?", "교내에서 편하게 입기 딱 좋은 후드티."],
                id1_to_att:[0,2,4,4,4,8,8,8,8,8,12,16],
                id1_to_range:[0,3,4,2,3,1,2,3,3,3,2,2],
                id12_to_def:[2,2,2,2,6,6,6,6,10,14,0,0,0,0,0,0],
                id12_to_hlt:[0,0,0,0,0,0,0,0,0,0,2,2,1,1,2,2],
                title: this.id
            })
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
        font-size: 7.2em;
        line-height: 3;
    }
</style>
