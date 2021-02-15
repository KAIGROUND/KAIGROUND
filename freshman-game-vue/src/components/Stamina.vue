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
                            :color="getCol((item-1)*5)"
                            :value="(item-1)*5"
                            style="height: 12px"
                            :buffer-value="(item-1)*5 === 0 ? 0 : 100"
                            stream
                            rounded
                    />
                </td>
                <td style="width:10%; padding: 0 0 0 12px">{{ item+13 }}</td>
                <td style="width:40%">
                    <v-progress-linear
                            :color="getCol(item*2+45)"
                            :value="item*2+45"
                            style="height: 12px"
                            :buffer-value="(item*2+45)*5 === 0 ? 0 : 100"
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
        methods: {
            getCol: val => {
                if(val > 66) return 'green';
                else if(val > 33) return 'orange';
                else if(val === 0) return 'blue';
                else return 'red darken-2'
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
