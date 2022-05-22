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
  main {
    text-align: center;
    padding: 1em;
    max-width: 240px;
    margin: 0 auto;
  }

  h1 {
    text-transform: uppercase;
    font-size: 1em;
    font-weight: 400;
  }

  h2 {
	  color:grey;
    font-size: 1em;
  }

  .main-verification-input {
    background: #fff;
    padding: 0 120px 0 0;
    border-radius: 1px;
    margin-top: 6px;
  }

  .fl-wrap {
    float: left;
    width: 100%;
    position: relative;
    border-radius: 4px;
  }

  .main-verification-input:before {
    content: "";
    position: absolute;
    bottom: -40px;
    width: 50px;
    height: 1px;
    background: rgba(255, 255, 255, 0.41);
    left: 50%;
    margin-left: -25px;
  }

  .main-verification-input-item {
    float: left;
    width: 100%;
    box-sizing: border-box;
    border-right: 1px solid #eee;
    height: 50px;
    position: relative;
  }

  .main-verification-input-item input:first-child {
    border-radius: 100%;
  }

  .main-verification-input-item input {
    float: left;
    border: none;
    width: 100%;
    height: 50px;
    padding-left: 20px;
  }

  .main-verification-button {
    background: #ff0030;
  }

  .main-verification-button {
    position: absolute;
    right: 0px;
    height: 50px;
    width: 120px;
    color: #fff;
    top: 0;
    border: none;
    border-top-right-radius: 4px;
    border-bottom-right-radius: 4px;
    cursor: pointer;
  }

  .main-verification-input-wrap {
    max-width: 500px;
    margin: 20px auto;
    position: relative;
    margin-top: 129px;
  }

  .answer {
	  margin-top: 27%;
	  background-color: white;
	 border-radius: 4px;
	 padding-bottom: 3px;
  }

  .main-verification-input-wrap ul {
    background-color: #fff;
    padding: 27px;
    color: #757575;
    border-radius: 4px;
  }

  a {
    text-decoration: none !important;
    color: #9c27b0;
  }

  :focus {
    outline: 0;
  }

  @media only screen and (max-width: 768px) {
    .main-verification-input {
      background: rgba(255, 255, 255, 0.2);
      padding: 14px 20px 10px;
      border-radius: 10px;
      box-shadow: 0px 0px 0px 10px rgba(255, 255, 255, 0);
    }

    .main-verification-input-item {
      width: 100%;
      border: 1px solid #eee;
      height: 50px;
      border: none;
      margin-bottom: 10px;
    }

    .main-verification-input-item input {
      border-radius: 6px !important;
      background: #fff;
    }

    .main-verification-button {
      position: relative;
      float: left;
      width: 100%;
      border-radius: 6px;
    }
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>