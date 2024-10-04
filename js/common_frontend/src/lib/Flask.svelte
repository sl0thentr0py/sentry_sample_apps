<script>
import { onMount } from 'svelte';

onMount(async () => {
  fetch("http://localhost:5000/count")
    .then(response => response.text())
    .then(data => {
        console.log(data);
      }).catch(error => {
          console.log(error);
      });
});
</script>

<h1> Flask </h1>count
