import { useState } from "react";

function SearchBar() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSearch = async () => {
    if (!query.trim()) return;
    setLoading(true);
    setResponse("");

    try {
      const res = await fetch("https://chatbot-backend-2cur.onrender.com/query", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ query }),
      });

      const data = await res.json();
      setResponse(data.response || "Sin respuesta.");
    } catch (error) {
      setResponse("Error al conectar con el servidor.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-xl mx-auto">
      <input
        className="border border-gray-300 rounded-md p-2 w-full mb-2"
        type="text"
        placeholder="Escribe tu pregunta..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && handleSearch()}
      />
      <button
        onClick={handleSearch}
        className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition"
        disabled={loading}
      >
        {loading ? "Buscando..." : "Buscar"}
      </button>

      {response && (
        <div className="mt-4 p-4 border bg-gray-100 rounded shadow">
          <strong>Respuesta:</strong>
          <p className="mt-2">{response}</p>
        </div>
      )}
    </div>
  );
}

export default SearchBar;
