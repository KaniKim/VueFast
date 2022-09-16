<template>
  <transition
      leave-class="translate-x-0"
      leave-active-class="transition ease-in-out duration-300 transform"
      leave-to-class="-translate-x-full"
  >
    <BarDrawer class="absolute" v-if="showSidebar"></BarDrawer>
  </transition>
  <div class="relative flex min-h-screen">

    <div class="flex-1">
      <div class="flex bg-white shadow px-2 py-4">
        <button @click="showSidebar = !showSidebar" class="text-cyan-600 font-extrabold">
          <svg style="margin-left: 10px" xmlns="http://www.w3.org/2000/svg" class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
          </svg>
        </button>
        <span style="padding-left: 30px" class="text-2xl font-extrabold text-blue-800">일취월장 음식 메뉴 정해주는 사이트</span>
      </div>
    </div>
  </div>
</template>
<script>
import {ref} from "vue";
import BarDrawer from "@/components/LayoutComponent/BarDrawer";

export default {
  components: {BarDrawer},
  setup() {
    const showSidebar = ref(false)
    return {
      showSidebar
    }
  }
}
</script>
<style>
.smooth-enter-active, .smooth-leave-active {
  transition: opacity .5s;
}
.smooth-enter, .smooth-leave-to {
  opacity: 0
}
</style>