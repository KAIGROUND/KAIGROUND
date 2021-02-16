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
                <div class="game-progressing-sub">슬라이드 {{page}}페이지 입니다.</div>
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
                            @click="dialog1 = false"
                    >
                        실패
                    </v-btn>
                    <v-btn
                            color="green darken-1"
                            text
                            @click="dialog1 = false"
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
                <div>
                    <v-img width="300px" height="300px" src="../assets/logo.png" @click="confirm(0)"></v-img>
                    <div class="text-wrapper"><span class="count">7</span>개 남음</div>
                </div>

                <div>
                    <v-img width="300px" height="300px" src="../assets/logo.png" @click="confirm(1)"></v-img>
                    <div class="text-wrapper"><span class="count">7</span>개 남음</div>
                </div>
                <div>
                    <v-img width="300px" height="300px" src="../assets/logo.png" @click="confirm(2)"></v-img>
                    <div class="text-wrapper"><span class="count">7</span>개 남음</div>
                </div>
            </v-row>
        </v-card>

    </v-container>
</template>

<script>
    export default {
        name: "Minigame",
        methods: {
            confirm(idx){
                this.idx=idx
                this.dialog_c=true
            },
            start(){
                this.dialog_c=false
                this.dialog=true
                this.page=123
                setTimeout(() => {
                    this.dialog=false
                    this.dialog1=true

                }, 5000)
            }
        },
        data(){
            return({
                dialog: false,
                dialog1: false,
                dialog_c: false,
                page: -1,
                idx: -1,
                img_src: 'https://i.pinimg.com/originals/0a/4d/cb/0a4dcb92fa2d3c601b58d72720d6bec4.jpg'
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
