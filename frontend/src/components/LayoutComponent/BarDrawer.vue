<template>
  <v-navigation-drawer>
    <v-list :items="items"></v-list>
  </v-navigation-drawer>
</template>
<script>
export default {
  data: () => ({
    group: null,
    items: [
      {
        title: 'Korean Food',
        value: 'foo',
      },
      {
        title: 'Chinese Food',
        value: 'bar',
      },
      {
        title: 'Japanese Food',
        value: 'fizz',
      },
      {
        title: 'Western Food',
        value: 'buzz',
      },
    ],
  }),
}
</script>
