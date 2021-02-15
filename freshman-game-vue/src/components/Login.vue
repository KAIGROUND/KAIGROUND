<template>
    <!-- https://codesandbox.io/s/0q4kvj8n0l?file=/src/main.js -->
    <v-app id="inspire">
        <v-content>
            <v-container fluid fill-height>
                <v-layout align-center justify-center>
                    <v-flex xs12 sm8 md4>
                        <v-card class="elevation-12">
                            <v-toolbar dark color="primary">
                                <v-toolbar-title>Login to KAIground</v-toolbar-title>
                            </v-toolbar>
                            <v-card-text>
                                <v-form>
                                    <v-text-field
                                            prepend-icon="person"
                                            name="login"
                                            label="Login"
                                            type="text"
                                            v-model="id"
                                    ></v-text-field>
                                    <v-text-field
                                            id="password"
                                            prepend-icon="lock"
                                            name="password"
                                            label="Password"
                                            type="password"
                                            v-model="pw"
                                    ></v-text-field>
                                </v-form>
                            </v-card-text>
                            <v-card-actions>
                                <v-spacer></v-spacer>
                                <v-btn color="primary" @click="submit">Login</v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-flex>
                </v-layout>
            </v-container>
        </v-content>
    </v-app>
</template>

<script>
    const md5 = require('md5')
    export default {
        name: "Login",
        data(){
            return({
                id: '',
                pw: ''
            })
        },
        methods: {
            submit(){

                //console.log(this.$store.state.class)
                //let passwd = ["5a6d935", "b0c8260", "d3454b3", "23afb7b", "5f2dd02", "0cfdee4", "bb33c82", "bd75bed", "8506f42", "2f2fdd7", "38d9924", "8c587a1", "1c90a1f", "5d573b6", "bcc3d15", "e2aede3", "c8598e5", "75311b4", "d35dad6", "dfcf865", "e3e14ed", "5c53d72", "20d48be", "2f3174b", "8f282ae", "ae7d478"]
                if(!isNaN(this.id) && parseInt(this.id) > 0 && parseInt(this.id) <= 26 && this.pw === md5('KAI' + this.id+ 'ground').toString().substring(0, 7)){
                    this.$store.commit('currentUser', this.id)
                    this.$router.push('/');

                }
                else alert("Login Failed!")
            }
        }
    }
</script>

<style scoped>

</style>
