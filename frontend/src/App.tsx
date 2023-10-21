import React, { useState } from "react";
import logo from "./assets/logo.svg";
import InputCourse from "./components/InputCourse";

export default function App() {
  const [courses, setCourses] = useState(Array(5).fill(""));

  const handleInputChange = (index: number, value: string) => {
    const newCourses = [...courses];
    newCourses[index] = value;
    setCourses(newCourses);
  };

  const BACKEND_URL =
    import.meta.env.REACT_APP_BACKEND_URL || "http://localhost:8000";

  const handleSubmit = async () => {
    try {
      const response = await fetch("${BACKEND_URL}/courses", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ courses }),
      });

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }

      const data = await response.json();
      console.log(data);
    } catch (error) {
      console.error("Error:", error);
    }
  };
  return (
    <main className="min-h-screen flex flex-col bg-gradient-to-br from-blue-200 to-blue-600">
      <header className="bg-blue-900 text-blue-200 p-2 w-full fixed top-0 left-0 z-10 flex justify-between items-center mb-auto">
        <h1 className="text-center font-bold text-xl">CupoSmart</h1>
      </header>
      <form className="flex-1 flex justify-center items-center bg-gray-200 py-2">
        <div className="bg-white p-8 rounded-lg shadow-md w-96">
          <div className="mt-4 flex justify-center">
            <img src={logo} alt="Logo de CupoSmart" className="w-1/2" />
          </div>
          <h1 className="text-xl font-bold mb-4">
            Agrega las siglas de tus ramos
          </h1>
          {[...Array(5)].map((_, idx) => (
            <InputCourse
              key={idx}
              number={idx + 1}
              value={courses[idx]}
              onChange={(value) => handleInputChange(idx, value)}
            />
          ))}
          <button
            onClick={handleSubmit}
            className="w-full bg-blue-500 hover:bg-blue-600 text-white p-2 rounded-md"
            aria-label="Calcular orden de inscripción"
          >
            Calcular orden inscripción
          </button>
        </div>
      </form>
      <footer className="text-center bg-blue-900 text-yellow-200 p-2 w-full mt-auto">
        <p className="font-semibold">CupoSmart © 2023</p>
      </footer>
    </main>
  );
}
