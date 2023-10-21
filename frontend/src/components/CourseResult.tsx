import React from "react";

interface CourseResultProps {
  courses: string[];
}

const CourseResult: React.FC<CourseResultProps> = ({ courses }) => {
  return (
    <div className="bg-white p-8 rounded-lg shadow-md w-96">
      <h1 className="text-xl font-bold mb-4">Resultados</h1>
      <ul>
        {courses.map((course, idx) => (
          <li key={idx}>{course}</li>
        ))}
      </ul>
    </div>
  );
};

export default CourseResult;
