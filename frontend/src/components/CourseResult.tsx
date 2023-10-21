import React from "react";

const CourseResult: React.FC<{ courses: string[] }> = ({ courses }) => {
  return (
    <div className="flex flex-col space-y-6 bg-white p-8 rounded-lg shadow-md w-96">
      <h1 className="text-xl font-bold mb-4">Orden recomendado</h1>
      {courses.map((course, idx) => (
        <div key={idx} className="flex space-x-4 items-center">
          <div className="rounded-full h-6 w-6 bg-gray-300 flex items-center justify-center">
            <span className="text-white text-sm font-bold">{idx + 1}</span>
          </div>
          <h2 className="text-lg font-medium text-gray-800">{course}</h2>
        </div>
      ))}
    </div>
  );
};

export default CourseResult;
