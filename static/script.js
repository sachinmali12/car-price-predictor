const form = document.getElementById("predictForm");
const resultDiv = document.getElementById("result");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    resultDiv.innerHTML = "⏳ Predicting...";

    const formData = new FormData(form);

    try {
        const response = await fetch("/predict", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        if (data.error) {
            resultDiv.innerHTML = "❌ Error: " + data.error;
        } else {
            resultDiv.innerHTML = `💰 ₹ ${data.prediction} Lakhs`;
        }

    } catch (err) {
        resultDiv.innerHTML = "❌ Server Error";
    }
});