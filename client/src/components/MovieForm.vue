<template>
  <div>
    <h2>{{ isEdit ? "Edit Movie" : "Add Movie" }}</h2>
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="title">Title:</label>
        <input
          v-model="form.title"
          type="text"
          id="title"
          class="form-control"
          required
        />
      </div>
      <div class="form-group">
        <label for="genre">Genre:</label>
        <input
          v-model="form.genre"
          type="text"
          id="genre"
          class="form-control"
          required
        />
      </div>
      <div class="form-group">
        <label for="director">Director:</label>
        <input
          v-model="form.director"
          type="text"
          id="director"
          class="form-control"
          required
        />
      </div>
      <div class="form-group">
        <label for="release_year">Release Year:</label>
        <input
          v-model="form.release_year"
          type="number"
          id="release_year"
          class="form-control"
          required
        />
      </div>
      <div class="form-group">
        <label for="rating">Rating:</label>
        <input
          v-model="form.rating"
          type="number"
          step="0.1"
          id="rating"
          class="form-control"
          required
        />
      </div>
      <div class="form-group">
        <label for="poster">Poster (optional):</label>
        <input type="file" @change="onFileChange" class="form-control" />
        <div v-if="existingPosterUrl" class="mt-2">
          <p>Current poster:</p>
          <img :src="existingPosterUrl" alt="Current Poster" width="120" />
        </div>
      </div>
      <button type="submit" class="btn btn-primary">
        {{ isEdit ? "Update" : "Add" }} Movie
      </button>
    </form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  props: ["id"], // Accept the id as a prop (via props:true in route definition)
  data() {
    return {
      form: {
        title: "",
        genre: "",
        director: "",
        release_year: "",
        rating: "",
        poster: null,
      },
      existingPosterUrl: null,
      isEdit: false,
    };
  },
  mounted() {
    const movieId = this.id; // Get the movie ID from the route params (now as a prop)
    if (movieId) {
      this.isEdit = true;
      this.fetchMovie(movieId); // Use the movieId to fetch movie details
    }
  },
  methods: {
    fetchMovie(movieId) {
      axios
        .get(`http://127.0.0.1:8000/api/movies/${movieId}/`)
        .then((response) => {
          this.form = { ...response.data, poster: null }; // Set form data with fetched movie details
          this.existingPosterUrl = response.data.poster; // Store URL for the existing poster
        })
        .catch((error) => {
          console.error("Error fetching movie:", error);
        });
    },
    submitForm() {
      if (this.isEdit) {
        this.updateMovie();
      } else {
        this.addMovie();
      }
    },
    updateMovie() {
      const movieId = this.id; // Get the movie ID from route params (as a prop)
      if (movieId) {
        const formData = new FormData();
        // Loop through the form data and append all fields
        for (let key in this.form) {
          formData.append(key, this.form[key]);
        }

        // Check if a new poster is selected, and only append if it's changed
        if (this.form.poster) {
          formData.append("poster", this.form.poster);
        }

        // Make the PUT request to update the movie
        axios
          .put(`http://127.0.0.1:8000/api/movies/${movieId}/`, formData, {
            headers: { "Content-Type": "multipart/form-data" },
          })
          .then(() => {
            this.$router.push("/"); // Redirect to home or movies list after update
          })
          .catch((error) => {
            console.error("Error updating movie:", error);
          });
      }
    },
    addMovie() {
      const formData = new FormData();
      // Append the form data to formData object
      formData.append("title", this.form.title);
      formData.append("genre", this.form.genre);
      formData.append("director", this.form.director);
      formData.append("release_year", this.form.release_year);
      formData.append("rating", this.form.rating);

      // Append the poster file if it's selected
      if (this.form.poster) {
        formData.append("poster", this.form.poster);
      }

      // Make the POST request to add the movie
      axios
        .post("http://127.0.0.1:8000/api/movies/", formData, {
          headers: { "Content-Type": "multipart/form-data" },
        })
        .then(() => {
          // Redirect to home or movie list page after adding the movie
          this.$router.push("/");
        })
        .catch((error) => {
          console.error("Error adding movie:", error);
        });
    },
    onFileChange(event) {
      this.form.poster = event.target.files[0]; // Update poster file if selected
    },
  },
};
</script>
