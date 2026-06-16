document.getElementById("fareForm").addEventListener("submit", function (event) {
    event.preventDefault();

    let formData = {
        trip_duration: parseFloat(document.getElementById("trip_duration").value),
        distance_traveled: parseFloat(document.getElementById("distance_traveled").value),
        num_of_passengers: parseInt(document.getElementById("num_of_passengers").value),
        surge_applied: parseFloat(document.getElementById("surge_applied").value)
    };

    console.log("📤 Sending Data:", formData);

    fetch("http://127.0.0.1:5000/predict", {  // Explicitly using localhost URL
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        console.log("📥 Received Response:", data);
        if (data.fare !== undefined) {
            document.getElementById("predictionResult").innerText = "Estimated Fare: $" + data.fare.toFixed(2);
        } else {
            document.getElementById("predictionResult").innerText = "Error: Unable to calculate fare.";
        }
    })
    .catch(error => {
        console.error("❌ Error:", error);
        document.getElementById("predictionResult").innerText = "Error: Something went wrong!";
    });
});
