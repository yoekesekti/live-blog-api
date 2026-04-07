console.log("🔥 Script jalan");

const API_URL = "http://127.0.0.1:8000/api/blogs";

// ========================
// LOAD DATA
// ========================
async function loadMessages() {
  try {
    console.log("⏳ Fetching...");

    const response = await fetch(API_URL);

    if (!response.ok) {
      throw new Error("Fetch gagal");
    }

    const data = await response.json();
    console.log("✅ Data:", data);

    const container = document.getElementById("postsContainer");
    const total = document.getElementById("totalMessages");

    container.innerHTML = "";

    if (!data.length) {
      container.innerHTML = "<p>Tidak ada pesan</p>";
      total.innerText = 0;
      return;
    }

    // tampilkan terbaru di atas
    data.slice().reverse().forEach(msg => {
      const card = document.createElement("div");
      card.className = "message-card";

      card.innerHTML = `
        <div>${msg.content}</div>
        <div class="author">👤 ${msg.author}</div>
        <div class="timestamp">⏱️ ${msg.timestamp}</div>
      `;

      container.appendChild(card);
    });

    total.innerText = data.length;

  } catch (err) {
    console.error("❌ ERROR:", err);
  }
}

// ========================
// INIT
// ========================
document.addEventListener("DOMContentLoaded", () => {
  console.log("🚀 UI Ready");
  loadMessages();
});
