async function askQuestion() {
    const question = document.getElementById("question").value;
    const platform = document.getElementById("platform").value;
    const responseBox = document.getElementById("response");

    // Clear previous response
    responseBox.innerHTML = "Loading...";

    try {
        const response = await fetch("/ask", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ question, platform }),
        });

        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status}`);
        }

        const data = await response.json();

        if (data.answer && Array.isArray(data.answer)) {
            responseBox.innerHTML = data.answer
                .map((res, idx) => `<p>${idx + 1}. ${res.content}</p>`)
                .join("");
        } else {
            responseBox.innerHTML = "No valid response from the backend.";
        }
    } catch (error) {
        console.error("Error:", error);
        responseBox.innerHTML = "An error occurred while processing your question.";
    }
}