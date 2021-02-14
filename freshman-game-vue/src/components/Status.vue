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
                            <v-text-field dark dense hide-details>

                            </v-text-field>
                        </v-col>
                        <v-col cols="6" class="pt-2 pb-2 ">
                            <span>구역으로 이동</span>
                        </v-col>
                        <v-col cols="3" class="icon-button">
                            <v-icon dark @click="run_attack">mdi-play-circle-outline</v-icon>
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
                            <v-text-field dark dense hide-details>

                            </v-text-field>
                        </v-col>
                        <v-col cols="2" class="pt-2 pb-2">
                            <span>반에</span>
                        </v-col>
                        <v-col cols="3" class="pt-1">
                            <v-select
                                    :items="my_attack_item"
                                    label="공격 아이템"
                                    hide-details
                                    dark
                                    dense
                            ></v-select>
                        </v-col>
                        <v-col cols="2" class="pt-2 pb-2">
                            <span>사용</span>
                        </v-col>
                        <v-col cols="2" class="icon-button">
                            <v-icon dark @click="run_attack">mdi-play-circle-outline</v-icon>
                        </v-col>
                    </v-row>


                </v-card>
            </v-col>
        </v-row>

        <v-row no-gutters dense>
            <v-col cols="12">
                <v-card class="ma-1 pa-2 text-center" color="indigo">
                    <v-row no-gutters dense>
                        <v-col class="pt-2 pb-2" cols="2">
                            <span>방어: </span>
                        </v-col>
                        <v-col class="pt-1" cols="1">
                            <v-select
                                    :items="my_attack_item"
                                    label="공격"
                                    hide-details
                                    dark
                                    dense
                            ></v-select>
                        </v-col>
                        <v-col class="pt-2 pb-2" cols="3">
                            <span>반의 </span><span class="font-weight-bold">{{"칼"}}</span> <span> 공격을</span>
                        </v-col>
                        <v-col class="pt-1" cols="3">
                            <v-select
                                    :items="my_attack_item"
                                    label="공격 아이템"
                                    hide-details
                                    dark
                                    dense
                            ></v-select>
                        </v-col>
                        <v-col class="pt-2 pb-2" cols="2">
                            <span>(으)로 방어</span>
                        </v-col>
                        <v-col cols="1" class="icon-button">
                            <v-icon dark @click="run_attack">mdi-play-circle-outline</v-icon>
                        </v-col>
                    </v-row>
                </v-card>
            </v-col>
        </v-row>
    </div>
</template>

<script>
    export default {
        name: "Status",
        data(){
            return({
                my_attack_item: ["칼", "knife", "sword", "검"]
            })
        },
        methods:{
            run_attack: () => {
                alert("attack!")
            }
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
