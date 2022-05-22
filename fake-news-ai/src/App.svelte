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

<main>
  <div class="row">
    <div class="col-md-12">
      <div class="main-verification-input-wrap">
        <ul>
          <li>
            In order to verify your news we offer you this simple AI. The AI
            will respond by <span style="color:#DA2C43; font-size:18px;">Fake</span> or
            <span style="color:#16d509f2; font-size:18px;">Real</span>.
          </li>
          <li>Enter that news below.</li>
        </ul>
        <div class="main-verification-input fl-wrap">
          <div class="main-verification-input-item">
            <input
              type="text"
              bind:value={news}
              placeholder="Enter your news here..."
            />
          </div>
          <button class="main-verification-button" on:click={getAnswer}>Verify Now</button>
        </div>

        <div class="answer" style="visibility:{visibility}">
			  <h2>Your news is <span style="color:indigo">{percent}</span> : </h2>
          	<h1 style="color:{color}">{answer}</h1>
        </div>
      </div>
    </div>
    <div style="visibility: {loading};">
      <Stretch size="60" color="#FFFFFF" unit="px" duration="1s"></Stretch>
    </div>
  </div>
</main>

<style>
</style>
