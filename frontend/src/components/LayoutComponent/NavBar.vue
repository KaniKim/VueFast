<template>
  <div>
    <div
        :class="open ? 'bg-red-500 opacity-25':'opacity-100'"
        class="absolute top-0 left-0 h-screen w-screen"
    >
      <button @click="tog()" class="text-black text-2xl p-2 font-bold">&#9776;</button>
    </div>
    <nav
        :class="open ? 'navbar-open' : 'navbar-close'"
        class="navbar w-64 absolute overflow-x-scroll bg-gray-700 top-0 h-screen"
    >
      <div class="flex pr-2 justify-end">
        <button @click="tog()" class="p-2 text-white text-xl font-bold">&#9747;</button>
      </div>
      <h1 class="text-xl text-center font-bold pt-5">Menu</h1>
      <ul class="list-none text-white text-center">
        <li class="my-8">
          <a href="#"></a>Teams
        </li>
        <li class="my-8">
          <a href="#"></a>Projects
        </li>
        <li class="my-8">
          <a href="#"></a>Favourites
        </li>
        <li class="my-8">
          <a href="#"></a>Notifications
        </li>
        <li class="my-8">
          <a href="#"></a>Members
        </li>
      </ul>
    </nav>
  </div>
</template>

<script>

export default {
  name: "App",
  data() {
    return {
      open: false
    };
  },
  methods: {
    tog() {
      this.open = !this.open;
    }
  }
};
</script>