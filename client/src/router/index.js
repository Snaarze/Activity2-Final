import { createRouter, createWebHistory } from "vue-router";
import MovieList from "@/components/MovieList.vue";
import MovieForm from "@/components/MovieForm.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: MovieList, // This is where your movie list will be shown
  },
  {
    path: "/edit/:id", // Path for editing a movie
    name: "EditMovie",
    component: MovieForm, // This will show the form for editing
    props: true, // Pass the id as a prop to MovieForm
  },
  {
    path: "/add", // Path for adding a new movie
    name: "AddMovie",
    component: MovieForm, // This will show the form for adding
    props: false, // No id needed for adding a movie
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
