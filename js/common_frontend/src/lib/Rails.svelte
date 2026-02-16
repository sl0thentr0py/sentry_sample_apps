<script>
import { onMount } from 'svelte';

onMount(async () => {
  fetch("http://localhost:3000/error")
    .then(response => response.text())
    .then(data => {
        console.log(data);
      }).catch(error => {
          console.log(error);
      });
});
</script>

<h1> Rails </h1>error
