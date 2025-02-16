document.getElementById("cropForm").addEventListener("submit", async function(event) {
    event.preventDefault();  // Prevent default form submission

    let data = {
        temperature: document.getElementById("temperature").value,
        humidity: document.getElementById("humidity").value,
        ph: document.getElementById("ph").value,
        rainfall: document.getElementById("rainfall").value
    };

    try {
        let response = await fetch("/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });

        let result = await response.json();

        // ✅ Check for errors in Flask response
        if (result.error) {
            document.getElementById("result").innerHTML = "Error: " + result.error;
        } else {
            document.getElementById("result").innerHTML = "Recommended Crop: " + result.crop;
        }

    } catch (error) {
        document.getElementById("result").innerHTML = "Server Error: " + error;
    }
});
