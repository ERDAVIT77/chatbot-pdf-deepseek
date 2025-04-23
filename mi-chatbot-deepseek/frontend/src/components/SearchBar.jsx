import { useState } from "react";

function SearchBar() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");

  const handleSearch = async () => {
    const res = await fetch(`http://localhost:8000/ask?q=${encodeURIComponent(query)}`);
    const data = await res.json();
    setResponse(data.answer);
  };

  return (
    <div>
      <input
        className="border p-2 w-full mb-2"
        type="text"
        placeholder="Escribe tu pregunta..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />
      <button onClick={handleSearch} className="bg-blue-500 text-white px-4 py-2 rounded">Buscar</button>
      {response && <div className="mt-4 p-4 border bg-gray-100">{response}</div>}
    </div>
  );
}

export default SearchBar;
