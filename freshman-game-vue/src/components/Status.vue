<template>
    <div>
        <v-row no-gutters dense>
            <v-col cols="5">
                <v-card class="ma-1 pa-2 text-center" color="indigo">
                    <v-row no-gutters dense>
                        <v-col cols="2" class="pt-2 pb-2">
                            <span>이동: </span>
                        </v-col>
                        <v-col cols="1">
                            <v-text-field dark dense hide-details :disabled="move_disable" v-model="move_pos">

                            </v-text-field>
                        </v-col>
                        <v-col cols="6" class="pt-2 pb-2 ">
                            <span>구역으로 이동</span>
                        </v-col>
                        <v-col cols="3" class="icon-button">
                            <v-icon dark @click="run_move" :disabled="move_disable">mdi-play-circle-outline</v-icon>
                        </v-col>
                    </v-row>


                </v-card>
            </v-col>


            <v-col cols="7">
                <v-card class="ma-1 pa-2 text-center" color="indigo">
                    <v-row no-gutters dense>
                        <v-col cols="2" class="pt-2 pb-2">
                            <span>공격:</span>
                        </v-col>
                        <v-col cols="1">
                            <v-text-field dark dense hide-details v-model="attack_classroom" :disabled="attack_disable">

                            </v-text-field>
                        </v-col>
                        <v-col cols="2" class="pt-2 pb-2">
                            <span>반에</span>
                        </v-col>
                        <v-col cols="3" class="pt-1">
                            <v-select
                                    :items="Object.keys(inventory_attack).map(x => id_to_item[x])"
                                    label="공격 아이템"
                                    hide-details
                                    dark
                                    dense
                                    :disabled="attack_disable"
                                    v-model="attack_item"
                            ></v-select>
                        </v-col>
                        <v-col cols="2" class="pt-2 pb-2">
                            <span>사용</span>
                        </v-col>
                        <v-col cols="2" class="icon-button">
                            <v-icon dark @click="run_attack" :disabled="attack_disable">mdi-play-circle-outline</v-icon>
                        </v-col>
                    </v-row>


                </v-card>
            </v-col>
        </v-row>

        <v-row no-gutters dense>
            <v-col cols="12">
                <v-card class="ma-1 pa-2 text-center" color="indigo">
                    <v-row no-gutters dense>
                        <v-col class="pt-2 pb-2" cols="1">
                            <span>방어: </span>
                        </v-col>
                        <v-col class="pt-1" cols="1">
                            <v-select
                                    :items="Object.keys(team_list)"
                                    label="공격"
                                    hide-details
                                    v-model="defense_team"
                                    dark
                                    dense
                                    :disabled="defense_disable"
                            ></v-select>
                        </v-col>
                        <v-col class="pt-2 pb-2" cols="4">
                            <span>반의 </span><span class="font-weight-bold">{{id_to_item[team_list[defense_team]]}}</span> <span> 공격을</span>
                        </v-col>
                        <v-col class="pt-1" cols="3">
                            <v-select
                                    :items="Object.keys(inventory_defense).map(x => id_to_item[x])"
                                    label="방어 아이템"
                                    hide-details
                                    dark
                                    dense
                                    v-model="defense_item"
                                    :disabled="defense_disable"
                            ></v-select>
                        </v-col>
                        <v-col class="pt-2 pb-2" cols="2">
                            <span>(으)로 방어</span>
                        </v-col>
                        <v-col cols="1" class="icon-button">
                            <v-icon dark @click="run_defense" :disabled="defense_disable">mdi-play-circle-outline</v-icon>
                        </v-col>
                    </v-row>
                </v-card>
            </v-col>
        </v-row>

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

    </div>
</template>

<script>
    export default {
        name: "Status",
        data(){
            return({
                attack_classroom: '',
                move_pos: '',
                snackbar: false,
                snackbar_text: '',
                move_disable: this.mode !== 0,
                attack_disable: this.mode !== 1,
                defense_disable: this.mode !== 1,
                defense_team: 0,
                defense_item: 0,
                attack_item: 0,
                id_to_item:['','개강','퀴즈','무거운 전공책','아침 수업','기숙사 호실이동','연습반','과제','실험 수업','계절 학기','중간고사','기말고사','예습복습','낮잠','야식','튜터링','족보','공강','딸기 파티','축제','라이프','수강 철회','카이 야잠','카이 돕바','청바지','카고바지','체크남방','카이 후드티'],
            })
        },
        props: ['mode', 'turn', 'inventory_attack', 'inventory_defense', 'team_list'],
        methods:{
            run_attack(){
                this.$http.post(`${this.$host}attack`, {
                    "me": this.$store.state.class,
                    "classroom": this.attack_classroom,
                    "pw": this.$store.state.pw,
                    "item": this.id_to_item.indexOf(this.attack_item)
                }).then(result => {
                    if(result.data.result !== 0){
                        this.snackbar_text = result.data.err_msg ?? '알 수 없는 오류가 발생했습니다.'
                        this.snackbar = true
                    } else {
                        this.snackbar_text = result.data.suc_msg +'\n점수 및 스테미나는 시간 종료 후 일괄 표시됩니다.'
                        this.snackbar = true
                        this.attack_disable = true
                        this.$emit('ainv', JSON.parse(result.data.attack_list))
                    }
                })
            },
            run_move(){
                this.$http.post(`${this.$host}move`, {
                    "me": this.$store.state.class,
                    "pw": this.$store.state.pw,
                    "area": this.move_pos,
                    "initial": this.turn === 1 ? 0 : 1
                }).then(result => {
                    if(result.data.result !== 0){
                        this.snackbar_text = result.data.err_msg ?? '알 수 없는 오류가 발생했습니다.'
                        this.snackbar = true
                    } else {
                        this.snackbar_text = result.data.suc_msg+'\n팀 이동은 시간 종료 후 일괄 표시됩니다.'
                        this.snackbar = true
                        this.move_disable = true
                    }
                })
            },
            run_defense(){
                this.$http.post(`${this.$host}defense`, {
                    "me": this.$store.state.class,
                    "classroom": this.defense_team,
                    "pw": this.$store.state.pw,
                    "item": this.id_to_item.indexOf(this.defense_item)
                }).then(result => {
                    if(result.data.result !== 0){
                        this.snackbar_text = result.data.err_msg ?? '알 수 없는 오류가 발생했습니다.'
                        this.snackbar = true
                    } else {
                        this.snackbar_text = result.data.suc_msg +'\n점수 및 스테미나는 시간 종료 후 일괄 표시됩니다.'
                        this.snackbar = true
                        this.$emit('dinv', JSON.parse(result.data.defense_list))
                    }
                })
            },

        },
        watch:{
            mode(val){
                if(val === 0){
                    this.move_disable = false
                    this.attack_disable = true
                    this.defense_disable = true
                }
                else if(val === 1){
                    this.move_disable = true
                    this.attack_disable = false
                    this.defense_disable = false
                } else {
                    this.move_disable = true
                    this.attack_disable = true
                    this.defense_disable = true
                }
            },
        }
    }
</script>

<style scoped>
    span {
        font-size: 1em;
        color: white;
    }

    .icon-button{
        padding-top: 6px;
    }
</style>
