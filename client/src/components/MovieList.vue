<template>
  <div class="container mt-4">
    <SearchBar @search="searchMovies" />
    <div class="row">
      <!-- Check if there are no movies yet -->
      <div v-if="movies.length === 0" class="col-12">
        <p>No movies yet</p>
      </div>

      <!-- Check if there are filtered movies or if search resulted in no matches -->
      <div v-else class="card-container">
        <!-- Show "No movies found" if no filtered movies match the search -->
        <div v-if="filteredMovies.length === 0" class="col-12">
          <p>No movies found</p>
        </div>

        <!-- Display MovieCard components for the filtered movies -->
        <div
          v-for="movie in filteredMovies"
          :key="movie.id"
          class="col-12 col-sm-6 col-md-4 col-lg-3 mb-4"
        >
          <MovieCard :movie="movie" @edit="editMovie" @delete="deleteMovie" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import MovieCard from "./MovieCard.vue";
import SearchBar from "./SearchBar.vue";

export default {
  components: { MovieCard, SearchBar },
  data() {
    return {
      movies: [],
      searchTerm: "",
    };
  },
  computed: {
    filteredMovies() {
      return this.movies.filter(
        (m) =>
          m.title.toLowerCase().includes(this.searchTerm.toLowerCase()) ||
          m.genre.toLowerCase().includes(this.searchTerm.toLowerCase())
      );
    },
  },
  methods: {
    fetchMovies() {
      axios
        .get("http://127.0.0.1:8000/api/movies/")
        .then((res) => (this.movies = res.data));
    },
    editMovie(movie) {
      this.$router.push({ name: "EditMovie", params: { id: movie.id } });
    },
    deleteMovie(id) {
      axios
        .delete(`http://127.0.0.1:8000/api/movies/${id}/`)
        .then(() => this.fetchMovies());
    },
    searchMovies(query) {
      this.searchTerm = query;
    },
  },
  mounted() {
    this.fetchMovies();
  },
};
</script>

<style>
.card-container {
  display: flex;
  width: 100%;
  flex-direction: row;
  gap: 2rem;
}
</style>
