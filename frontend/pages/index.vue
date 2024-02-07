<script setup>

    let message = ref("")
    let response = ref("")
    const sendMessage = async () => {
        //message.value;
        const {data: answer} = await useFetch('http://localhost:8000/chatbot/',{
            method: 'POST',
            body:{
                question: message
            }
        })
        response.value = answer.value
    }
</script>

<template>
    <div>
        <label for=""> Type here your message!</label> <br>
        <textarea v-model="message"/> <br> <br> 
        <Button @click="sendMessage" label="Send A message"></Button>
        <hr>
        <div>
            <h5>Bard: 😊</h5>
            <p>{{ response.content }}</p>
        </div>

        <TextBox avatarImage="sergiao.png" name="Segiao" message="slv bot" side="left"> </TextBox>
        <TextBox avatarImage="gat.png" name="Sr.Gato" message="Slv segião" side="right"> </TextBox>
    </div>
</template>

<style scoped>
     

</style>