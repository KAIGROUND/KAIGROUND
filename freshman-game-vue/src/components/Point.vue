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
                <td style="width:10%; padding: 0 0 0 12px">{{ item }}</td>
                <td style="text-align: center; font-weight: bold">{{point_list[item] ? point_list[item] : 0}}</td>
                <td style="width:10%; padding: 0 0 0 12px">{{ item + 13 }}</td>
                <td style="text-align: center; font-weight: bold">{{point_list[item+13] ? point_list[item+13] : 0}}</td>
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
