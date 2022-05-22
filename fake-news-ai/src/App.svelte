<script lang="ts">
  import { Stretch } from "svelte-loading-spinners";

  let loading: string = "hidden";
  let visibility: string = "hidden";
  let answer: string = "fake";
  let percent: string = "0%";
  let color: string = "#DA2C43";
  let news: string = "";

  const getAnswer = () => {
    visibility = "hidden";
    loading = "unset";
    fetch("./postrand", {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ news }),
    })
      .then((res) => res.json())
      .then((data) => {
        answer = data.response;
        percent = data.percent;
        answer == "fake" ? (color = "#DA2C43") : (color = "#16d509f2");
        visibility = "unset";
        loading = "hidden";
      })
      .catch((err) => {
        console.log(err);
      });
  };
</script>

<main>Hello</main>

<style>
</style>
