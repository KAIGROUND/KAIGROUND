<template>
    <v-card class="ma-2">
        <!--        <v-card-title>Map</v-card-title>-->
        <div class="title grey darken-3 white--text">
            <span>Stamina</span>
        </div>
        <v-divider></v-divider>
        <v-simple-table>
            <tbody>
            <tr v-for="item in 13" :key="item" :bgcolor="item%2 ? '#EEEEEE': ''">
                <td style="width:10%; padding: 0 0 0 12px" :class="class_accent(item)" @mouseover="$emit('class_accent', item)" @mouseleave="$emit('class_restore')">{{ item }}</td>
                <td style="width:40%" :class="class_accent(item)" @mouseover="$emit('class_accent', item)" @mouseleave="$emit('class_restore')">
                    <div style="text-align: center">
                        <v-progress-linear
                                :color="getCol(st(item))"
                                :value="st(item)"
                                style="height: 12px; margin-top: 12px; margin-bottom: -4px"
                                :buffer-value="st(item) === 0 ? 0 : 100"
                                stream
                                rounded
                        />
                        <span style="font-size: 0.8em;">{{st(item)/10 === 0 ? 'respawn...' : st(item)/10}}</span>
                    </div>

                </td>
                <td style="width:10%; padding: 0 0 0 12px" :class="class_accent(item+13)" @mouseover="$emit('class_accent', item+13)" @mouseleave="$emit('class_restore')">{{ item+13 }}</td>
                <td style="width:40%" :class="class_accent(item+13)"  @mouseover="$emit('class_accent', item+13)" @mouseleave="$emit('class_restore')">
                    <div style="text-align: center">
                        <v-progress-linear
                                :color="getCol(st(item+13))"
                                :value="st(item+13)"
                                style="height: 12px; margin-top: 12px; margin-bottom: -4px"
                                :buffer-value="st(item+13) === 0 ? 0 : 100"
                                stream
                                rounded
                        />
                        <span style="font-size: 0.8em;">{{st(item+13)/10 === 0 ? 'respawn...' : st(item+13)/10}}</span>
                    </div>
                </td>
            </tr>
            </tbody>
        </v-simple-table>
    </v-card>
</template>

<script>
    export default {
        name: "Stamina",
        data(){
            return ({
                stamina_list: []
            })
        },
        methods: {
            getCol(val){
                if(val > 132) return 'green';
                else if(val > 66) return 'orange';
                else if(val === 0) return 'blue';
                else return 'red darken-2'
            },
            st(idx){
                return this.stamina_list[idx]?this.stamina_list[idx]:0;
            },
            class_accent(idx){
                return this.$store.state.class === idx.toString() ? 'amber lighten-3' : ''
            },
        },
        mounted() {
            const stamina = this.$firebase.database().ref('stamina')
            stamina.on("value", snapshot => {
                for(let i in snapshot.val()){
                    this.$set(this.stamina_list, i, snapshot.val()[i]*20)
                }
            })
        }, 
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
    tr:nth-child(2n+1):hover {
        background-color: #EEEEEE !important;
    }
    tr:nth-child(2n):hover {
        background-color: transparent !important;
    }
</style>
