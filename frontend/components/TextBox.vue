<script setup>
const props = defineProps({
  avatarImage: { type: String },
  name: { type: String },
  message: { type: String },
  side: { type: String },
});



</script>

<template>
  <div>
    <Fieldset :class="props.side == 'left'? 'answer' : 'question'">
      <template #legend>
        <div class="flex align-items-center pl-2">
          <Avatar :image="props.avatarImage" shape="circle" />
          <span class="font-bold">{{ props.name }}</span>
        </div>
      </template>
      <p class="m-0">
        {{ props.message }}
      </p>
    </Fieldset>
  </div>
</template>

<style scoped lang="scss">

/*.p-fieldset-legend > div {
    background-color: v-bind(cardStyle.color);
    font-size: v-bind(cardStyle.size)
}*/

.answer .p-fieldset-legend > div {
    background-color: pink;
    font-size: 15px;

}

.question{
    .p-fieldset-legend > div {
        background-color: purple;
        font-size: 30px;
        width: 95vw;
        justify-content:;
    }
    .p-toggleable-content .p-fieldset-content p {
        background-color: blue;
        color:white;
    }
} 

    

</style>