export default function InputCourse({
  number,
  value,
  onChange,
}: {
  number: number;
  value: string;
  onChange: (val: string) => void;
}) {
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
        aria-label={`Ingrese el curso ${number}`}
        className="w-full p-2 border rounded-md"
      />
    </div>
  );
}
