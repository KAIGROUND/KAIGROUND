<template>
    <v-card class="ma-2">
<!--        <v-card-title>Map</v-card-title>-->
        <div class="title grey darken-3 white--text ">
            <span>Map</span>
        </div>
        <v-divider/>
        <v-img
                max-height="620px"
                src="../assets/map.png"
        >
            <v-switch v-model="switch1" inset class="switch-me" :label="switch1 ? '팀 수 표시' : '구역 표시'"></v-switch>

            <div v-for="(i, idx) in this.node" :key="idx" @mouseover="mouseover(idx)" @mouseleave="mouseleave" @mousemove="mousemove">
                <v-btn style="position: relative"
                       elevation="2"
                       fab
                       :color="i.cur_team.includes(parseInt($store.state.class)) ? 'pink' : 'indigo'"
                       class="fab-small"
                       :style="'position:absolute;left: '+(i.pos[0]-50)+'px; top: '+(i.pos[1]-165)+'px;color:white'"
                >{{switch1 ? i.cur_team.length ? i.cur_team.length:'' : idx+1}}</v-btn>
            </div>

        </v-img>
        <v-menu
                v-model="showMenu"
                absolute
                offset-y
                :position-x="last_hovered[0]"
                :position-y="last_hovered[1]"
                style="max-width: 600px"
        >
            <v-card
                    class="mx-auto"
                    max-width="344"
                    outlined
            >
                <v-list-item three-line>
                    <v-list-item-content>
                        <div class="overline mb-2">
                            {{'구역 ' + (hover+1)}}
                        </div>
                        <v-list-item-title class="headline mb-1">
                            {{node[hover].name}}
                        </v-list-item-title>
                        <div class="mt-4"/>
                        <v-list-item-subtitle>
                            {{node[hover].cur_team.length > 0 ? '현재 위치한 팀' : ''}}

                            <v-chip-group column>
                                <v-chip
                                        v-for="team in node[hover].cur_team"
                                        :key="team"
                                        :value="team"
                                        :class=" team === parseInt($store.state.class) ? 'pink white--text':'indigo accent-4 white--text'"
                                >
                                    {{ team }}
                                </v-chip>
                            </v-chip-group>
<!--                            {{node[hover].cur_team.length > 0 ? `현재 위치한 팀: ${node[hover].cur_team.toString()}` : ''}}-->
                        </v-list-item-subtitle>
                    </v-list-item-content>

                    <v-list-item-avatar
                            tile
                            size="80"
                            color="grey"
                    ></v-list-item-avatar>
                </v-list-item>
            </v-card>
        </v-menu>
    </v-card>

</template>

<script>
    export default {
        name: "Map",
        props: {},
        data(){
            return({
                pos: [[162,353],[191,362],[223,361],[224,264],[242,293],[248,316],[242,340],[251,361],[266,352],[294,344],[344,361],[372,387],[385,432],[346,454],[327,414],[300,385],[276,385],[237,417],[213,478],[174,466],[137,501],[140,536],[171,587],[246,587],[267,525],[252,502],[323,505],[364,507],[395,505],[434,518],[474,503],[506,474],[614,544],[570,544],[521,594],[471,578],[415,601],[434,636],[406,552],[371,551],[372,614],[334,706]],
                name: ["건물 1", "건물 2", "건물 ㅁㄴㅇㄹ", "건물 2", "건물 fds", "건물 2", "건물 1", "건물 2", "건물 1", "건물 2", "건물 1", "건물 2", "건물 1", "건물 2", "건물 1", "건물 2", "건물 1", "건물 2", "건물 1", "건물 2", "건물 1", "건물 2", "건물 1", "건물 2", "건물 1", "건물 2", "건물 1", "건물 2", "건물 1", "건물 2", "건물 1", "건물 2", "건물 1", "건물 2", "건물 1", "건물 2", "건물 1", "건물 2", "건물 1", "건물 2", "건물 1", "건물 2"],
                node:[],
                switch1:false,
                hover:0,
                last_hovered:[0,0],
                showMenu:false,
            })
        },
        methods: {
            mouseover(idx){
                this.hover = idx
                this.showMenu = true
            },
            mouseleave(){
                this.showMenu=false
            },
            mousemove(event){
                this.last_hovered = [event.clientX + 40, event.clientY]
            }
        },
        created() {
            for(let i = 0; i < 42; i++){
                this.node.push({
                    pos: this.pos[i],
                    name: this.name[i],
                    cur_team: [],
                })
            }
            this.node[2].cur_team.push(21)
            this.node[2].cur_team.push(5)
            this.node[21].cur_team.push(7)
            this.node[21].cur_team.push(12)
            this.node[22].cur_team.push(2)
        },
        computed:{
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
    .fab-small{
        width: 20px !important;
        height: 20px !important;
    }
    .switch-me{
        position:absolute;
        margin-left: 500px;
    }
</style>
