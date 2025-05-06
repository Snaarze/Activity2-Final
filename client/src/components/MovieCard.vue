<template>
  <div class="card m-2" style="width: 18rem">
    <img
      :src="movie.poster"
      class="card-img-top"
      alt="Poster"
      style="width: 100%; height: 200px; object-fit: cover"
    />
    <div class="card-body">
      <h5 class="card-title">{{ movie.title }}</h5>
      <p class="card-text">
        Genre: {{ movie.genre }}<br />Director: {{ movie.director }}
      </p>
      <button class="btn btn-sm btn-warning me-1" @click="$emit('edit', movie)">
        Edit
      </button>
      <button class="btn btn-sm btn-danger" @click="$emit('delete', movie.id)">
        Delete
      </button>
    </div>
  </div>
</template>

<script>
export default {
  props: ["movie"],
};
</script>
