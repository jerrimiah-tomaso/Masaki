console.log("MASAKI V1 loaded!");

const backendStatus = document.getElementById("status");

fetch("http://127.0.0.1:8000/")
  .then((response) => response.json())
  .then((data) => {
    if (data.message === "active") {
      backendStatus.innerText = "Backend: Active";
    }
    console.log(data.message);
  });
