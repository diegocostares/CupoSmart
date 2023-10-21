import React from "react";
import InputCourse from "./InputCourse";
import logo from "../assets/logo.svg";

interface CourseFormProps {
  courses: string[];
  onInputChange: (index: number, value: string) => void;
  onSubmit: () => void;
}

const CourseForm: React.FC<CourseFormProps> = ({
  courses,
  onInputChange,
  onSubmit,
}) => {
  return (
    <div className="bg-white p-8 rounded-lg shadow-md w-96">
      <div className="mt-4 flex justify-center">
        <img src={logo} alt="Logo de CupoSmart" className="w-1/2" />
      </div>
      <h1 className="text-xl font-bold mb-4">Agrega las siglas de tus ramos</h1>
      {[...Array(5)].map((_, idx) => (
        <InputCourse
          key={idx}
          number={idx + 1}
          value={courses[idx]}
          onChange={(value) => onInputChange(idx, value)}
        />
      ))}
      <button
        onClick={onSubmit}
        className="w-full bg-blue-500 hover:bg-blue-600 text-white p-2 rounded-md"
        aria-label="Calcular orden de inscripción"
      >
        Calcular orden inscripción
      </button>
    </div>
  );
};

export default CourseForm;
