<template>
    <!-- https://codesandbox.io/s/0q4kvj8n0l?file=/src/main.js -->
    <v-app id="inspire">
        <v-content>
            <v-container fluid fill-height>

                <v-layout align-center justify-center>
                    <v-flex xs12 sm8 md4>
                        <v-img src="../assets/kaiground.png"></v-img>
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
                        <v-img src="../assets/freshman-ot.png" height="200px" width="300px" style="margin: 0 auto"></v-img>
                    </v-flex>
                </v-layout>
            </v-container>
        </v-content>
    </v-app>
</template>

<script>
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
                this.$http.post(`${this.$host}login`, {
                    "me": this.id,
                    "pw": this.pw,
                }).then(result => {
                    if(result.data.result === 0){
                        this.$store.commit('currentUser', this.id)
                        this.$store.commit('currentPw', this.pw)
                        this.$router.push('/');
                    } else {
                        alert("Login Failed!")
                    }
                })
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
