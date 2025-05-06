<template>
  <input
    type="text"
    class="form-control my-3"
    placeholder="Search by title or genre"
    v-model="searchQuery"
    @input="$emit('search', searchQuery)"
  />
</template>

<script>
export default {
  data() {
    return {
      searchQuery: "",
    };
  },
};
</script>
