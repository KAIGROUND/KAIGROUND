<template>
    <v-container>

        <v-dialog
                v-model="dialog_c"
                persistent
                max-width="500"
        >
            <v-card >
                <v-card-title class="headline font-weight-bold">
                    확인
                </v-card-title>
                <v-card-text>{{idx+1}}번째 아이템을 선택하신 것이 맞나요?</v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn
                            color="red darken-1"
                            text
                            @click="dialog_c = false"
                    >
                        취소
                    </v-btn>
                    <v-btn
                            color="green darken-1"
                            text
                            @click="start()"
                    >
                        확인
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>

        <v-dialog
                v-model="dialog"
                persistent
                max-width="1000"
        >
            <v-card>
                <div class="game-progressing">{{idx + 1}}번째 아이템을 얻기 위한 미니게임이 진행 중입니다.</div>
                <div class="game-progressing-sub">{{msg}}</div>
            </v-card>
        </v-dialog>

        <v-dialog
                v-model="dialog1"
                persistent
                max-width="500"
        >
            <v-card >
                <v-card-title class="headline font-weight-bold">
                    미니게임 성공 여부
                </v-card-title>
                <v-card-text>미니게임에 성공하셨나요? 아래 버튼을 눌러주세요.</v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn
                            color="red darken-1"
                            text
                            @click="miniresult(1)"
                    >
                        실패
                    </v-btn>
                    <v-btn
                            color="green darken-1"
                            text
                            @click="miniresult(0)"
                    >
                        성공
                    </v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>

        <v-card class="ma-2">
            <div class="title grey darken-3 white--text ">
                <span>Minigame</span>
            </div>
            <v-row justify="space-around" class="pa-8">
                <div @click="confirm(0)">
                    <div>
                        <InventoryDesc :id="prices[0].item1" narrow="true" style="display: inline-block; vertical-align: top"></InventoryDesc>
                        <InventoryDesc :id="prices[0].item2" narrow="true" style="display: inline-block; vertical-align: top"></InventoryDesc>
                    </div>
                    <div class="text-wrapper"><span class="count">{{prices[0].cnt}}</span>개 남음</div>
                </div>
                <div @click="confirm(1)">
                    <div>
                        <InventoryDesc :id="prices[1].item1" narrow="true" style="display: inline-block; vertical-align: top"></InventoryDesc>
                        <InventoryDesc :id="prices[1].item2" narrow="true" style="display: inline-block; vertical-align: top"></InventoryDesc>
                    </div>
                    <div class="text-wrapper"><span class="count">{{prices[1].cnt}}</span>개 남음</div>
                </div>
                <div @click="confirm(2)">
                    <div>
                        <InventoryDesc :id="prices[2].item1" narrow="true" style="display: inline-block; vertical-align: top"></InventoryDesc>
                        <InventoryDesc :id="prices[2].item2" narrow="true" style="display: inline-block; vertical-align: top"></InventoryDesc>
                    </div>
                    <div class="text-wrapper"><span class="count">{{prices[2].cnt}}</span>개 남음</div>
                </div>
            </v-row>
        </v-card>

        <v-snackbar v-model="snackbar">
            {{ snackbar_text }}

            <template v-slot:action="{ attrs }">
                <v-btn
                        color="pink"
                        text
                        v-bind="attrs"
                        @click="snackbar = false"
                >
                    Close
                </v-btn>
            </template>
        </v-snackbar>

    </v-container>
</template>

<script>
    import InventoryDesc from "./InventoryDesc";
    export default {
        name: "Minigame",
        components: {InventoryDesc},
        props: ["prices"],
        methods: {
            confirm(idx){
                this.idx=idx
                this.dialog_c=true
            },
            start(){
                this.dialog_c=false
                this.$http.post(`${this.$host}miniselect`, {
                    "me": this.$store.state.class,
                    "select": this.idx
                }).then(result => {
                    if (result.data.result === 0) {
                        this.msg = result.data.msg
                        this.dialog = true
                        setTimeout(() => {
                            this.dialog = false
                            this.dialog1 = true
                        }, 10000)
                    } else if (result.data.result === 1) {
                        this.snackbar_text = '다른 팀에서 먼저 선택해 현재 수량이 0입니다. 다른 세트를 선택해 주세요.'
                        this.snackbar = true
                    } else {
                        this.snackbar_text = result.data.err_msg ?? '알 수 없는 오류가 발생했습니다.'
                        this.snackbar = true
                    }
                })
            },
            miniresult(res){
                this.dialog1=false
                this.$http.post(`${this.$host}minisuccess`, {
                    "me": this.$store.state.class,
                    "select": this.idx,
                    "success": res
                }).then(result => {
                    if (result.data.result === 0) {
                        this.$emit('minidone')
                    } else {
                        this.snackbar_text = result.data.err_msg ?? '알 수 없는 오류가 발생했습니다.'
                        this.snackbar = true
                    }
                })
            }
        },
        data(){
            return({
                dialog: false,
                dialog1: false,
                dialog_c: false,
                idx: -1,
                snackbar: false,
                snackbar_text: '',
                msg: '',
            })
        }
    }
</script>

<style scoped>
    .count{
        font-size: 5em;
    }

    .text-wrapper{
        text-align: center;
    }

    .title{
        text-align: center;
        padding: 8px;
    }
    .title > span{
        font-size: 1.2em;
    }

    .game-progressing{
        font-size: 2em;
        text-align: center;
        padding: 24px;
        font-weight: bold;
    }

    .game-progressing-sub{
        font-size: 1em;
        text-align: center;
        padding: 24px;
    }
</style>
