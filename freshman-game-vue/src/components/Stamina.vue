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
                <td style="width:10%; padding: 0 0 0 12px">{{ item }}</td>
                <td style="width:40%">
                    <v-progress-linear
                            :color="getCol(st(item))"
                            :value="st(item)"
                            style="height: 12px"
                            :buffer-value="st(item) === 0 ? 0 : 100"
                            stream
                            rounded
                    />
                </td>
                <td style="width:10%; padding: 0 0 0 12px">{{ item+13 }}</td>
                <td style="width:40%">
                    <v-progress-linear
                            :color="getCol(st(item+13))"
                            :value="st(item+13)"
                            style="height: 12px"
                            :buffer-value="st(item+13) === 0 ? 0 : 100"
                            stream
                            rounded
                    />
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
                if(val > 66) return 'green';
                else if(val > 33) return 'orange';
                else if(val === 0) return 'blue';
                else return 'red darken-2'
            },
            st(idx){
                return this.stamina_list[idx]?this.stamina_list[idx]:0;
            }
        },
        mounted() {
            const stamina = this.$firebase.database().ref('stamina')
            stamina.on("value", snapshot => {
                for(let i in snapshot.val()){
                    this.$set(this.stamina_list, i, snapshot.val()[i]*10)
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
</style>
