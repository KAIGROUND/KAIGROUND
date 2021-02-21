<template>
    <div class="overlay noto">
        <div>
            <div class="right-container">
                <div class="r-rank1 oswald">{{'#' + result_data.rank}}</div>
                <div class="r-rank2 oswald">/26</div>
            </div>

            <div class="left-container">
                <div class="white--text large-header">{{$store.state.class + '반'}}</div>
                <div class="amber--text normal-header">{{rank_subtitle}}</div>
            </div>


            <div class="main-container">
                <div class="white--text normal-header mr-8">랭킹</div>
                <div class="white--text normal-header oswald">{{'#' + result_data.rank}}</div>
                <div class="spec-container">
                    <div class="white--text normal-header mb-10 flex">재운 횟수<div class="white--text oswald ml-8">{{this.result_data.kill_cnt}}</div> 회</div>
                    <div class="white--text normal-header mb-10 flex">수면 횟수<div class="white--text oswald ml-8">{{this.result_data.sleep_cnt}}</div> 회</div>
                    <div class="white--text normal-header flex">이동한 칸<div class="white--text oswald ml-8">{{this.result_data.move_cnt}}</div> 회</div>
                </div>
            </div>

            <v-btn class="right-bottom" @click="$emit('close')">
                나가기
           </v-btn>

        </div>


    </div>
</template>

<script>
    export default {
        name: "Result",
        props: ["show", "result_data"],
        computed: {
            rank_subtitle(){
                return this.result_data.rank === 1 ? '이겼닭! 오늘 저녁은 치킨이닭!' : this.result_data.rank <= 3 ? `TOP ${this.result_data.rank} 달성!` : this.result_data.rank <= 10 ? 'TOP 10 달성!' : ''
            }
        }
    }
</script>

<style scoped>
    @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@500&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@300&display=swap');
    @import url('https://fonts.googleapis.com/css?family=Noto+Sans+KR&display=swap');


    .overlay{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 10;
        background-color: rgba(0,0,0,0.8); /*dim the background*/
    }
    .right-container{
        display: flex;
        position: absolute;
        right: 30px;
        top: 10px;
        left: auto;
        align-items: flex-end;
    }
    .r-rank1{
        font-weight:500;
        font-size: 6em;
        color: #FFC107;
    }
    .r-rank2{
        font-weight:300;
        font-size: 5em;
        padding-bottom: 4px;
        color: rgba(255,255,255,0.4);
    }
    .left-container{
        position: absolute;
        left: 50px;
        top: 30px;
    }

    .normal-header{
        font-size: 3em;
    }

    .large-header{
        font-size: 4em;
    }

    .main-container{
        display: flex;
        position: absolute;
        left: 50px;
        top: 250px;
    }

    .spec-container{
        margin-left: 100px;
    }

    .oswald{
        font-family: 'Oswald',sans-serif;
    }

    .flex{
        display: flex;
    }

    .noto{
        font-family: 'NOTO Sans KR', sans-serif;
    }

    .right-bottom{
        position: absolute;
        right: 50px;
        bottom: 50px;
    }
</style>
