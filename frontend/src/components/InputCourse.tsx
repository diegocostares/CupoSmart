export default function InputCourse({ number }: { number: number }) {
  return (
    <div className="mb-4">
      <label
        htmlFor={`course-${number}`}
        className="block text-sm font-bold mb-2"
      >{`Curso ${number}`}</label>
      <input
        id={`course-${number}`}
        type="text"
        aria-label={`Ingrese el curso ${number}`}
        className="w-full p-2 border rounded-md"
      />
    </div>
  );
}
