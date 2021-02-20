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
                                <v-btn color="pink" class="white--text" @click="freshman_submit">새내기로 로그인</v-btn>
                                <v-btn color="primary" @click="submit">로그인</v-btn>
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
                if(!isNaN(this.id) && parseInt(this.id) > 0 && parseInt(this.id) <= 26 && this.pw === md5('KAI' + this.id+ 'ground').toString().substring(0, 7)){
                    this.$store.commit('currentUser', this.id)
                    this.$router.push('/');

                }
                else alert("Login Failed!")
            },
            freshman_submit(){
                this.$store.commit('currentUser', "0")
                this.$router.push('/');
            }
        }
    }
</script>

<style scoped>

</style>
