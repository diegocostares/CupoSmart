import React, { useState, useEffect } from "react";
import logo from "./assets/logo.svg";
import InputCourse from "./components/InputCourse";
import CourseForm from "./components/CourseForm";
import CourseResult from "./components/CourseResult";

export default function App() {
  const [courses, setCourses] = useState(Array(5).fill(""));
  const [showResults, setShowResults] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [availableCourses, setAvailableCourses] = useState([]);
  const [banner, setBanner] = useState("");

  const handleInputChange = (index: number, value: string) => {
    const newCourses = [...courses];
    newCourses[index] = value;
    setCourses(newCourses);
  };

  const BACKEND_URL =
    import.meta.env.VITE_BACKEND_URL || "http://localhost:8000";

  useEffect(() => {
    // Cargar los cursos disponibles desde el backend
    const loadAvailableCourses = async () => {
      try {
        const response = await fetch(`${BACKEND_URL}/courses`);
        if (!response.ok) {
          throw new Error("Failed to fetch available courses");
        }
        const data = await response.json();
        setAvailableCourses(data.courses || []);
      } catch (error) {
        console.error("Error loading available courses:", error);
      }
    };

    loadAvailableCourses();
  }, []);

  const handleSubmit = async () => {
    setIsLoading(true);
    console.log({ courses, banner: Number(banner) });
    try {
      const response = await fetch(`${BACKEND_URL}/courses`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ courses, banner: Number(banner) }),
      });

      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      const data = await response.json();
      console.log(data);
      setShowResults(true);
    } catch (error) {
      console.error("Error:", error);
      setShowResults(false);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <main className="min-h-screen flex flex-col bg-gradient-to-br from-blue-200 to-blue-600">
      <header className="bg-blue-900 text-blue-200 p-2 w-full fixed top-0 left-0 z-10 flex justify-between items-center mb-auto">
        <h1 className="text-center font-bold text-xl">CupoSmart</h1>
      </header>
      <div className="flex-1 flex justify-center items-center bg-gray-200 py-2">
        {isLoading ? (
          <div className="border-gray-300 h-20 w-20 animate-spin rounded-full border-8 border-t-blue-600" />
        ) : !showResults ? (
          <CourseForm
            courses={courses}
            availableCourses={availableCourses}
            banner={banner}
            onBannerChange={setBanner}
            onInputChange={handleInputChange}
            onSubmit={handleSubmit}
          />
        ) : (
          <CourseResult courses={courses} />
        )}
      </div>
      <footer className="text-center bg-blue-900 text-yellow-200 p-2 w-full mt-auto">
        <p className="font-semibold">CupoSmart © 2023</p>
      </footer>
    </main>
  );
}
