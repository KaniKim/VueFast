<template>
  <div
    class="relative flex min-h-screen flex-col justify-center overflow-hidden"
  >
    <div
      class="m-auto w-full rounded bg-white p-6 shadow-lg ring-2 ring-purple-800/50 lg:max-w-md"
    >
      <h1 class="text-center text-3xl font-semibold text-purple-700">LOGO</h1>

      <form class="mt-6">
        <div>
          <label for="email" class="block text-sm text-gray-800">Email</label>
          <input
            type="email"
            class="mt-2 block w-full rounded-md border bg-white px-4 py-2 text-purple-700 focus:border-purple-400 focus:outline-none focus:ring focus:ring-purple-300 focus:ring-opacity-40"
          />
        </div>
        <div class="mt-4">
          <div>
            <label for="password" class="block text-sm text-gray-800"
              >Password</label
            >
            <input
              type="password"
              class="mt-2 block w-full rounded-md border bg-white px-4 py-2 text-purple-700 focus:border-purple-400 focus:outline-none focus:ring focus:ring-purple-300 focus:ring-opacity-40"
            />
          </div>
          <a href="#" class="text-xs text-gray-600 hover:underline"
            >Forget Password?</a
          >
          <div class="mt-6">
            <button
              class="w-full rounded-md bg-purple-700 px-4 py-2 tracking-wide text-white transition-colors duration-200 hover:bg-purple-600 focus:bg-purple-600 focus:outline-none"
            >
              Login
            </button>
          </div>
        </div>
      </form>
      <p class="mt-8 text-center text-xs font-light text-gray-700">
        Don't have an account?
        <a href="#" class="font-medium text-purple-600 hover:underline"
          >Sign up</a
        >
      </p>
    </div>
  </div>
</template>
