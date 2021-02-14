<template>
    <v-card class="ma-2">
        <!--        <v-card-title>Map</v-card-title>-->
        <div class="title grey darken-3 white--text">
            <span>Point</span>
        </div>
        <v-divider></v-divider>
        <v-simple-table dense>
            <tbody>
            <tr v-for="item in 13" :key="item.name" :bgcolor="item%2 ? '#EEEEEE': ''">
                <td style="width:10%; padding: 0 0 0 12px">{{ item }}</td>
                <td style="text-align: center; font-weight: bold">{{item*15}}</td>
                <td style="width:10%; padding: 0 0 0 12px">{{ item + 13 }}</td>
                <td style="text-align: center; font-weight: bold">{{item}}</td>
            </tr>
            </tbody>
        </v-simple-table>
    </v-card>

</template>

<script>
    export default {
        name: "Point"
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
