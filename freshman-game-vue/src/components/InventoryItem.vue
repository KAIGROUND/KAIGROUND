<template>
    <div>
        <div id="container">

            <img width="48px" height="48px" style="vertical-align:middle; padding: 8px" :src="src">
            <span>{{name}}</span>

        </div>
    </div>
</template>

<script>
    export default {
        name: "InventoryItem",
        props:['src', 'name']
    }
</script>

<style scoped>
    span{
        font-size: 0.9em;
    }
    #container{
        height: 48px;
    }
</style>
