<template>
    <v-card class="ma-2">
<!--        <v-card-title>Map</v-card-title>-->
        <div class="title grey darken-3 white--text ">
            <span>Map</span>
        </div>
        <v-divider/>
        <v-img
                max-height="620px"
                src="../assets/map.png">

            <div class="map-info">맵 상의 정점 또는 오른쪽 스테미나에 커서를 갖다 대어 반 위치를 확인하세요.</div>
            <v-switch v-model="switch1" inset class="switch-me" :label="switch1 ? '팀 수 표시' : '구역 표시'"></v-switch>


            <div v-for="(i, idx) in this.node" :key="idx" @mouseover="mouseover(idx)" @mouseleave="mouseleave" @mousemove="mousemove">
                <v-btn style="position: relative"
                       elevation="2"
                       fab
                       :color="i.cur_team.includes(accent+'') ? 'orange' : i.cur_team.includes($store.state.class) ? 'pink' : 'indigo'"
                       class="fab-small"
                       :style="'position:absolute;left: '+(i.pos[0])+'px; top: '+(i.pos[1])+'px;color:white'"
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
                    max-width="454"
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
                                        :class="team == $store.state.class ? 'pink white--text':'indigo accent-4 white--text'"
                                >
                                    {{ team }}
                                </v-chip>
                            </v-chip-group>
<!--                            {{node[hover].cur_team.length > 0 ? `현재 위치한 팀: ${node[hover].cur_team.toString()}` : ''}}-->
                        </v-list-item-subtitle>
                    </v-list-item-content>

                    <v-list-item-avatar
                            tile
                            size="160"
                    >
                        <v-img width="160px" height="160px" :src="get_src(hover)">

                        </v-img>

                    </v-list-item-avatar>
                </v-list-item>
            </v-card>
        </v-menu>
    </v-card>
</template>

<script>
    export default {
        name: "Map",
        props: ['accent'],
        data(){
            return({
                pos: [[162,353],[191,362],[223,361],[224,264],[242,293],[248,316],[242,340],[251,361],[266,352],[294,344],[344,361],[372,387],[385,432],[346,454],[327,414],[300,385],[276,385],[237,417],[213,478],[174,466],[137,501],[140,536],[171,587],[246,587],[267,525],[252,502],[323,505],[364,507],[395,505],[434,518],[474,503],[506,474],[614,544],[570,544],[521,594],[471,578],[415,601],[434,636],[406,552],[371,551],[372,614],[334,706]],
                name: ["아름관","소망관","사랑관","지혜관","신뢰관","진리관","성실관","카이마루","우체국","교양분관","산업디자인학과동","인문사회과학부동","대강당","정문술빌딩","스포츠컴플렉스","장영신학생회관","태울관","기계공학동","노천극장","풍동실험동","미르나래관","인터내셔널빌리지","희망다솜관","어은동산","W8","KARA","KAIST본관","창의학습관","궁리실험관","자연과학동","의과학연구센터","세종관","파팔라도","운동장","나노종합기술원","정보전자공학동","KI빌딩","산업경영학동","교직원회관","학술문화관","오리연못","지오센트리퓨지실험동"],
                node:[],
                switch1:true,
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
            },
            get_src(idx){
                try{
                    return require('../assets/building/'+(idx+1)+'.jpg')
                } catch (e){
                    return ''
                }

            }
        },
        created() {
            for(let i = 0; i < 42; i++){
                this.node.push({
                    pos: [this.pos[i][0]*1.02-46, this.pos[i][1]*1.02-175],
                    name: this.name[i],
                    cur_team: [],
                })
            }
        },
        mounted() {
            const pos = this.$firebase.database().ref('pos')
            pos.on("value", snapshot => {
                for(let i=0; i < 42; i++){
                    this.node[i].cur_team=[]
                }


                for(let i in snapshot.val()){
                    if(snapshot.val()[i] !== 0){
                        this.node[snapshot.val()[i]-1].cur_team.push(i)
                    }
                }
            })
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
        right: 20px;
        top: 20px;
    }
    .map-info{
        top: 10px;
        right: 20px;
        position: absolute;
        font-size: 0.7em;
    }
</style>
