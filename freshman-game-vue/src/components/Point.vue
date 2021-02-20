<template>
    <v-card class="ma-2">
        <!--        <v-card-title>Map</v-card-title>-->
        <div class="title grey darken-3 white--text">
            <span>Point</span>
        </div>
        <v-divider></v-divider>
        <v-simple-table>
            <tbody>
            <tr v-for="item in 13" :key="item.name" :bgcolor="item%2 ? '#EEEEEE': ''">
                <td style="width:20%; padding: 0 0 0 12px;" :class="class_accent(item)">{{max_class(item)}}</td>
                <td style="width:30%; text-align: center; font-weight: bold" :class="class_accent(item)">{{point_list[item] ? point_list[item] : 0}}</td>
                <td style="width:20%; padding: 0 0 0 12px" :class="class_accent(item+13)">{{max_class(item + 13)}}</td>
                <td style="width:30%; text-align: center; font-weight: bold;" :class="class_accent(item+13)">{{point_list[item+13] ? point_list[item+13] : 0}}</td>
            </tr>
            </tbody>
        </v-simple-table>
    </v-card>

</template>

<script>
    export default {
        name: "Point",
        data(){
            return ({
                point_list: []
            })
        },
        mounted() {
            const point = this.$firebase.database().ref('point')
            point.on("value", snapshot => {
                for(let i in snapshot.val()){
                    this.$set(this.point_list, i, snapshot.val()[i])
                }
            })
        },
        methods: {
            class_accent(idx){
                return this.$store.state.class === idx.toString() ? 'amber lighten-3' : ''
            },
            max_class(idx){
                return idx;//(this.point_list.slice(0).sort(function(a,b){a<b})[0] === this.point_list[idx] && this.point_list[idx] !== 0) ? idx + '👑' : idx
            }
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
</style>
