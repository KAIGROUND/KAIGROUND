<template>
    <v-container class="container">
        <v-card class="card" color="indigo">
            <span>{{$store.state.class === "0" ? '새내기 여러분 환영합니다!' : $store.state.class + '반'}}</span>
            <v-btn color="pink" class="white--text" @click="logout">Logout</v-btn>
        </v-card>
    </v-container>
</template>

<script>
    export default {
        name: "Logout",
        methods:{
            logout(){
                this.$store.commit('currentUser', null)
                this.$router.push('/login')
            }
        }
    }
</script>

<style scoped>
    span{
        margin-right: 12px;
        color: white;
    }
    .card{
        padding: 12px 16px 12px 16px;
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
