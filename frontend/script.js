async function getWeather() {
    const location = document.getElementById("location").value;
    const resultDiv = document.getElementById("weather-result");

    if (!location) {
        resultDiv.innerHTML = `<p>Please enter a location.</p>`;
        return;
    }

    try {
        const response = await fetch("http://127.0.0.1:8000/weather", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ location: location })
        });

        if (!response.ok) {
            throw new Error("Failed to fetch weather. Check backend or CORS.");
        }

        const data = await response.json();
        const { description, temperature, wind_speed } = data;

        resultDiv.innerHTML = `
            <div class="card">
                <h2>📍 ${location}</h2>
                <p>🌤️ <strong>${description}</strong></p>
                <p>🌡️ Temperature: <strong>${temperature}°C</strong></p>
                <p>💨 Wind Speed: <strong>${wind_speed} km/h</strong></p>
            </div>
        `;
    } catch (error) {
        resultDiv.innerHTML = `<p>${error.message}</p>`;
    }
}
