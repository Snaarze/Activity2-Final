<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-primary mb-3">
    <div class="container-fluid">
      <router-link to="/" class="navbar-brand">🎬 Movie Collection</router-link>
      <div class="d-flex">
        <router-link to="/" class="btn btn-outline-light me-2"
          >Home</router-link
        >
        <router-link to="/add" class="btn btn-outline-light"
          >Add Movie</router-link
        >
      </div>
    </div>
  </nav>

  <div class="container mt-4">
    <div class="text-center mb-4">
      <h1 class="display-4 text-primary">My Movie Collection</h1>
    </div>
    <router-view></router-view>
  </div>
</template>

<script></script>

<style scoped>
/* Styling for Navbar */
.navbar {
  border-radius: 0.375rem;
}

/* Customizing button hover effect */
.btn-outline-light:hover {
  background-color: #ffffff;
  color: #007bff;
  transition: 0.3s ease;
}

/* Title Style */
h1.display-4 {
  font-size: 3rem;
  font-weight: 600;
  color: #343a40;
  letter-spacing: 2px;
}

/* Add custom spacing */
.container {
  padding: 20px;
}
</style>
