import React from "react";

interface InputCourseProps {
  number: number;
  value: string;
  availableCourses: string[];
  onChange: (val: string) => void;
}

export default function InputCourse({
  number,
  value,
  availableCourses,
  onChange,
}: InputCourseProps) {
  return (
    <div className="mb-4">
      <label
        htmlFor={`course-${number}`}
        className="block text-sm font-bold mb-2"
      >{`Curso ${number}`}</label>
      <input
        id={`course-${number}`}
        type="text"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        list="available-courses"
        aria-label={`Ingrese el curso ${number}`}
        className="w-full p-2 border rounded-md"
      />
      <datalist id="available-courses">
        {availableCourses.map((course) => (
          <option key={course} value={course} />
        ))}
      </datalist>
    </div>
  );
}
