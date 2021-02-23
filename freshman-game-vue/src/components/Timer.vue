<template>
    <v-dialog
            v-model="show"
            persistent
            width="440"
    >
        <v-card style="padding: 20px">
            <radial-progress-bar :diameter="400"
                                 :completed-steps="completedSteps"
                                 :total-steps="totalSteps"
                                 :strokeWidth="20"
                                 :innerStrokeWidth="19"
                                 innerStrokeColor="#AAAAAA"
                                 startColor="#303f9f"
                                 stopColor="#512da8"
                                 :isClockwise="false">
                <div class="num">{{this.completedSteps + 1}}</div>
            </radial-progress-bar>
        </v-card>
    </v-dialog>
</template>

<script>
    import RadialProgressBar from 'vue-radial-progress'

    export default {
        name: "Timer",
        props: ["show"],
        data () {
            return {
                completedSteps: 9,
                totalSteps: 9,
            }
        },
        mounted() {

        },
        watch: {
            show(){
                if(this.show){
                    this.completedSteps = 9;
                    let count = setInterval(() => {
                        this.completedSteps--
                        if(this.completedSteps < 0){
                            clearInterval(count)
                            this.$emit("show_cd", false)
                        }
                    }, 1000)
                }
            }
        },
        components: {
            RadialProgressBar
        }
    }
</script>

<style scoped>
    .num{
        font-family: 'Oswald',sans-serif;
        font-size: 5.0em;
    }
</style>
