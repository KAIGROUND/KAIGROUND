<template>
    <v-container class="container">
        <v-card class="card" color="indigo">
            <v-row no-gutters style="width: 400px">
                <v-col cols="1" class="white--text my-label">
                    id:
                </v-col>
                <v-col cols="3" class="text-center">
                    <v-text-field dense dark hide-details label="반">

                    </v-text-field>
                </v-col>
                <v-col col="1"/>
                <v-col cols="1" class="white--text my-label">
                    pw:
                </v-col>
                <v-col cols="3" class="text-center">
                    <v-text-field dense dark hide-details label="비밀번호" type="password">

                    </v-text-field>
                </v-col>
                <v-col cols="3" class="text-right">
                    <v-btn color="pink" class="white--text">Login</v-btn>
                </v-col>
            </v-row>
        </v-card>
    </v-container>
</template>

<script>
    export default {
        name: "Login"
    }
</script>

<style scoped>
    .card{
        padding: 12px 16px 8px 16px;
        max-width: fit-content;
        float: right;
    }
    .container{
        max-width: 1600px;
    }
    .my-label{
        text-align: center;
        line-height: 40px;
    }
</style>
