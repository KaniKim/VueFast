<template>
  <nav class="navber navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Soldout</a>
      <button
        class="navbar-target"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-o">
          <li class="nav-item">
            <router-link class="nav-link active" to="/">제품리스트</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/detail"
              >제품상세페이지</router-link
            >
          </li>
          <li v-if="(user.email = undefined)" class="nav-item">
            <router-link class="nav-link" to="/sales"
              >제품등록페이지</router-link
            >
          </li>
          <form class="d-flex">
            <input
              class="form-control me-2"
              type="search"
              placeholder="Saerch"
              aria-label="Search"
            />
            <button class="btn btn-outline-success" type="submit">
              Search
            </button>
          </form>
        </ul>
      </div>
    </div>
  </nav>
</template>
<script>
export default {
  name: "header",
};
</script>