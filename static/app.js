if ("serviceWorker" in navigator) {
    navigator.serviceWorker.register("/sw.js")
        .then(() => console.log("Service Worker зарегистрирован"))
        .catch((err) => console.error("Ошибка регистрации SW:", err));
}

const loadBtn = document.getElementById("load-btn");
if (loadBtn) {
    loadBtn.addEventListener("click", async () => {
        const city = document.getElementById("city").value;
        const days = document.getElementById("days").value;
        const output = document.getElementById("output");

        try {
            const response = await fetch(`/api/forecast/${city}?days=${days}`);
            const data = await response.json();
            output.textContent = `HTTP ${response.status}\n` + JSON.stringify(data, null, 2);
        } catch (err) {
            output.textContent = "Нет сети или сервер недоступен (офлайн-режим).";
        }
    });
}
